import { configureStore } from '@reduxjs/toolkit';
import uiReducer from './slices/uiSlice';
import interactionReducer from './slices/interactionSlice';
import agentReducer from './slices/agentSlice';

export const store = configureStore({
  reducer: {
    ui: uiReducer,
    interaction: interactionReducer,
    agent: agentReducer,
  },
});

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;
