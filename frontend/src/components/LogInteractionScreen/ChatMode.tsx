import React, { useState, useRef } from 'react';
import { useAppDispatch, useAppSelector } from '../../store/hooks';
import { addUserMessage, addAssistantChunk, setStreaming } from '../../store/slices/agentSlice';
import { AgentService } from '../../services/agent';

const ChatMode: React.FC = () => {
  const dispatch = useAppDispatch();
  const { messages, isStreaming } = useAppSelector((state) => state.agent);
  const [input, setInput] = useState('');
  const agentService = useRef(new AgentService());

  const sendMessage = () => {
    if (!input.trim() || isStreaming) return;
    const userMsg = input.trim();
    dispatch(addUserMessage(userMsg));
    setInput('');
    dispatch(setStreaming(true));

    agentService.current.stream(
      userMsg,
      (chunk) => {
        dispatch(addAssistantChunk(chunk));
      },
      () => {
        dispatch(setStreaming(false));
      },
      (error) => {
        console.error(error);
        dispatch(setStreaming(false));
      }
    );
  };

  return (
    <div className="chat-mode">
      <div className="messages">
        {messages.map((msg, idx) => (
          <div key={idx} className={`message ${msg.role}`}>
            <strong>{msg.role === 'user' ? 'You' : 'AI'}:</strong> {msg.content}
          </div>
        ))}
        {isStreaming && <div className="typing">AI is typing...</div>}
      </div>
      <div className="input-area">
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => e.key === 'Enter' && sendMessage()}
          placeholder="Type your request..."
          disabled={isStreaming}
        />
        <button onClick={sendMessage} disabled={isStreaming || !input.trim()}>
          Send
        </button>
      </div>
    </div>
  );
};

export default ChatMode;
