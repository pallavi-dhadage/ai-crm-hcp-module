import { createSlice, PayloadAction } from '@reduxjs/toolkit';

interface AgentState {
  messages: { role: 'user' | 'assistant'; content: string }[];
  isStreaming: boolean;
}

const initialState: AgentState = {
  messages: [],
  isStreaming: false,
};

const agentSlice = createSlice({
  name: 'agent',
  initialState,
  reducers: {
    addUserMessage: (state, action: PayloadAction<string>) => {
      state.messages.push({ role: 'user', content: action.payload });
    },
    addAssistantChunk: (state, action: PayloadAction<string>) => {
      const last = state.messages[state.messages.length - 1];
      if (last && last.role === 'assistant') {
        last.content += action.payload;
      } else {
        state.messages.push({ role: 'assistant', content: action.payload });
      }
    },
    setStreaming: (state, action: PayloadAction<boolean>) => {
      state.isStreaming = action.payload;
    },
    clearMessages: (state) => {
      state.messages = [];
    },
  },
});

export const { addUserMessage, addAssistantChunk, setStreaming, clearMessages } = agentSlice.actions;
export default agentSlice.reducer;
