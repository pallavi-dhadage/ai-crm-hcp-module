import React, { useState } from 'react';
import { useAppDispatch } from '../../store/hooks';
import { logInteraction } from '../../store/slices/interactionSlice';

const FormMode: React.FC = () => {
  const dispatch = useAppDispatch();
  const [form, setForm] = useState({
    hcp_name: '',
    interaction_type: 'meeting',
    interaction_date: '',
    notes: '',
  });

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    dispatch(logInteraction(form));
  };

  return (
    <form onSubmit={handleSubmit} className="form-mode">
      <input
        placeholder="HCP Name"
        value={form.hcp_name}
        onChange={(e) => setForm({ ...form, hcp_name: e.target.value })}
        required
      />
      <select
        value={form.interaction_type}
        onChange={(e) => setForm({ ...form, interaction_type: e.target.value })}
      >
        <option value="call">Call</option>
        <option value="meeting">Meeting</option>
        <option value="email">Email</option>
        <option value="lunch">Lunch</option>
        <option value="conference">Conference</option>
        <option value="other">Other</option>
      </select>
      <input
        type="date"
        value={form.interaction_date}
        onChange={(e) => setForm({ ...form, interaction_date: e.target.value })}
        required
      />
      <textarea
        placeholder="Notes"
        value={form.notes}
        onChange={(e) => setForm({ ...form, notes: e.target.value })}
        rows={4}
      />
      <button type="submit">Log Interaction</button>
    </form>
  );
};

export default FormMode;
