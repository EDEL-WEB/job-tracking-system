
import React from 'react';

const GradientForm = ({ form, onChange, onSubmit }) => {
  return (
    <form onSubmit={onSubmit}>
      <div className="row">
        <div className="col-md-6 mb-3">
          <label className="form-label">Gradient Name</label>
          <input
            type="text"
            className="form-control"
            value={form.gradientName}
            onChange={(e) => onChange({...form, gradientName: e.target.value})}
            required
          />
        </div>
        <div className="col-md-6 mb-3">
          <label className="form-label">Fruit Type</label>
          <select
            className="form-select"
            value={form.fruitType}
            onChange={(e) => onChange({...form, fruitType: e.target.value})}
            required
          >
            <option value="">Select Fruit</option>
            <option value="Orange">Orange</option>
            <option value="Apple">Apple</option>
            <option value="Banana">Banana</option>
            <option value="Mango">Mango</option>
            <option value="Pineapple">Pineapple</option>
            <option value="Watermelon">Watermelon</option>
          </select>
        </div>
      </div>
      
      <div className="row">
        <div className="col-md-4 mb-3">
          <label className="form-label">Quantity</label>
          <input
            type="text"
            className="form-control"
            value={form.quantity}
            onChange={(e) => onChange({...form, quantity: e.target.value})}
            required
          />
        </div>
        <div className="col-md-4 mb-3">
          <label className="form-label">Unit</label>
          <select
            className="form-select"
            value={form.unit}
            onChange={(e) => onChange({...form, unit: e.target.value})}
          >
            <option value="kg">kg</option>
            <option value="lbs">lbs</option>
            <option value="pieces">pieces</option>
          </select>
        </div>
        <div className="col-md-4 mb-3">
          <label className="form-label">Application Date</label>
          <input
            type="date"
            className="form-control"
            value={form.applicationDate}
            onChange={(e) => onChange({...form, applicationDate: e.target.value})}
            required
          />
        </div>
      </div>
      
      <div className="row">
        <div className="col-md-6 mb-3">
          <label className="form-label">Purpose</label>
          <input
            type="text"
            className="form-control"
            value={form.purpose}
            onChange={(e) => onChange({...form, purpose: e.target.value})}
            required
          />
        </div>
        <div className="col-md-6 mb-3">
          <label className="form-label">Notes</label>
          <textarea
            className="form-control"
            value={form.notes}
            onChange={(e) => onChange({...form, notes: e.target.value})}
            rows="2"
          />
        </div>
      </div>
      
      <button type="submit" className="btn btn-info">
        <i className="bi bi-droplet me-2"></i>
        Apply Gradient
      </button>
    </form>
  );
};

export default GradientForm;
