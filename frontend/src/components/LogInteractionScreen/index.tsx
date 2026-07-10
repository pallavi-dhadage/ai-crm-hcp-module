import React, { useState } from 'react';
import FormMode from './FormMode';
import ChatMode from './ChatMode';
import './styles.css';

const LogInteractionScreen: React.FC = () => {
  const [activeTab, setActiveTab] = useState<'form' | 'chat'>('form');

  return (
    <div className="container">
      <header className="header">
        <h1>Log HCP Interaction</h1>
        <div className="toggle-group">
          <button
            className={`toggle-btn ${activeTab === 'form' ? 'active' : ''}`}
            onClick={() => setActiveTab('form')}
          >
            📋 Form
          </button>
          <button
            className={`toggle-btn ${activeTab === 'chat' ? 'active' : ''}`}
            onClick={() => setActiveTab('chat')}
          >
            💬 Chat
          </button>
        </div>
      </header>
      <main className="content">
        {activeTab === 'form' ? <FormMode /> : <ChatMode />}
      </main>
    </div>
  );
};

export default LogInteractionScreen;
