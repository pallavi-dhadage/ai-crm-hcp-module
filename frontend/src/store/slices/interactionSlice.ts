import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import api from '../../services/api';

export interface Interaction {
  id: number;
  hcp_name: string;
  notes: string;
  ai_summary: string;
}

interface InteractionState {
  list: Interaction[];
  current: Interaction | null;
  loading: boolean;
  error: string | null;
}

const initialState: InteractionState = {
  list: [],
  current: null,
  loading: false,
  error: null,
};

export const logInteraction = createAsyncThunk(
  'interaction/log',
  async (data: any) => {
    const response = await api.post('/api/interactions', data);
    return response.data;
  }
);

const interactionSlice = createSlice({
  name: 'interaction',
  initialState,
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(logInteraction.pending, (state) => {
        state.loading = true;
        state.error = null;
      })
      .addCase(logInteraction.fulfilled, (state, action) => {
        state.loading = false;
        state.list.unshift(action.payload);
        state.current = action.payload;
      })
      .addCase(logInteraction.rejected, (state, action) => {
        state.loading = false;
        state.error = action.error.message || 'Failed';
      });
  },
});

export default interactionSlice.reducer;
