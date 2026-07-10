import { createSlice } from '@reduxjs/toolkit';

interface UIState {
  mode: 'form' | 'chat';
  loading: boolean;
}

const initialState: UIState = {
  mode: 'form',
  loading: false,
};

const uiSlice = createSlice({
  name: 'ui',
  initialState,
  reducers: {
    toggleMode: (state) => {
      state.mode = state.mode === 'form' ? 'chat' : 'form';
    },
    setLoading: (state, action) => {
      state.loading = action.payload;
    },
  },
});

export const { toggleMode, setLoading } = uiSlice.actions;
export default uiSlice.reducer;
