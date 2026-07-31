import React, { useState, useEffect, useRef } from 'react';
import { useNavigate } from 'react-router-dom';
import api from '../utils/api';

const Chat = () => {
  const [question, setQuestion] = useState('');
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const messagesEndRef = useRef(null);
  const navigate = useNavigate();

  // Проверяем, есть ли токен
  useEffect(() => {
    const token = localStorage.getItem('access_token');
    if (!token) {
      navigate('/login');
    }
  }, [navigate]);

  // Автоскролл к последнему сообщению
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!question.trim()) return;

    setLoading(true);
    setError('');

    // Добавляем вопрос пользователя в список
    const userMessage = { role: 'user', content: question };
    setMessages(prev => [...prev, userMessage]);
    setQuestion('');

    try {
      const response = await api.post('/chat/', { question });
      
      // Добавляем ответ бота
      const botMessage = { 
        role: 'bot', 
        content: response.data.answer,
        sources: response.data.sources || []
      };
      setMessages(prev => [...prev, botMessage]);
      
    } catch (err) {
      if (err.response && err.response.status === 401) {
        // Токен истёк — перенаправляем на логин
        localStorage.removeItem('access_token');
        localStorage.removeItem('refresh_token');
        navigate('/login');
      } else {
        setError('Ошибка при отправке запроса. Попробуйте позже.');
      }
    } finally {
      setLoading(false);
    }
  };

  const handleLogout = () => {
    localStorage.removeItem('access_token');
    localStorage.removeItem('refresh_token');
    navigate('/login');
  };

  return (
    <div className="container-fluid vh-100 d-flex flex-column">
      {/* Header */}
      <div className="row bg-light p-3 border-bottom">
        <div className="col d-flex justify-content-between align-items-center">
          <h3 className="m-0">🤖 Научный ассистент</h3>
          <button onClick={handleLogout} className="btn btn-outline-danger">
            Выйти
          </button>
        </div>
      </div>

      {/* Messages */}
      <div className="row flex-grow-1 overflow-auto p-3" style={{ maxHeight: 'calc(100vh - 180px)' }}>
        <div className="col">
          {messages.length === 0 && (
            <div className="text-center text-muted mt-5">
              <p>Задайте вопрос о науке и технологиях</p>
              <small>Например: "Что такое квантовый компьютер?"</small>
            </div>
          )}
          
          {messages.map((msg, index) => (
            <div key={index} className={`mb-3 ${msg.role === 'user' ? 'text-end' : 'text-start'}`}>
              <div className={`d-inline-block p-3 rounded-3 ${msg.role === 'user' ? 'bg-primary text-white' : 'bg-light border'}`}>
                <div style={{ maxWidth: '600px', whiteSpace: 'pre-wrap' }}>
                  {msg.content}
                </div>
                {msg.sources && msg.sources.length > 0 && (
                  <div className="mt-2 small text-secondary">
                    <strong>Источники:</strong> {msg.sources.map(s => s.title).join(', ')}
                  </div>
                )}
              </div>
            </div>
          ))}
          
          {loading && (
            <div className="text-start">
              <div className="d-inline-block p-3 bg-light border rounded-3">
                <span className="spinner-border spinner-border-sm me-2" role="status"></span>
                Думаю...
              </div>
            </div>
          )}
          
          {error && (
            <div className="alert alert-danger mt-3">
              {error}
            </div>
          )}
          
          <div ref={messagesEndRef} />
        </div>
      </div>

      {/* Input */}
      <div className="row bg-light p-3 border-top">
        <div className="col">
          <form onSubmit={handleSubmit} className="d-flex gap-2">
            <input
              type="text"
              className="form-control"
              placeholder="Введите ваш вопрос..."
              value={question}
              onChange={(e) => setQuestion(e.target.value)}
              disabled={loading}
            />
            <button type="submit" className="btn btn-primary" disabled={loading || !question.trim()}>
              Отправить
            </button>
          </form>
        </div>
      </div>
    </div>
  );
};

export default Chat;