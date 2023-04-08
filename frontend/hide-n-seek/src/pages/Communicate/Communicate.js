import React from 'react';
import './Communicate.css';

function Communicate() {
  return (
    <div className="cards-container">
      <div className="card">
        <div className="card-header">
          <h2>Card 1 Heading</h2>
        </div>
        <div className="card-body">
          <img src="https://via.placeholder.com/150" alt="card image" className="card-image" />
          <p>Card 1 description goes here</p>
        </div>
        <div className="card-footer">
          <button className="card-button">Button 1</button>
        </div>
      </div>

      <div className="card">
        <div className="card-header">
          <h2>Card 2 Heading</h2>
        </div>
        <div className="card-body">
          <img src="https://via.placeholder.com/150" alt="card image" className="card-image" />
          <p>Card 2 description goes here</p>
        </div>
        <div className="card-footer">
          <button className="card-button">Button 2</button>
        </div>
      </div>

      <div className="card">
        <div className="card-header">
          <h2>Card 3 Heading</h2>
        </div>
        <div className="card-body">
          <img src="https://via.placeholder.com/150" alt="card image" className="card-image" />
          <p>Card 3 description goes here</p>
        </div>
        <div className="card-footer">
          <button className="card-button">Button 3</button>
        </div>
      </div>

      <div className="card">
        <div className="card-header">
          <h2>Card 4 Heading</h2>
        </div>
        <div className="card-body">
          <img src="https://via.placeholder.com/150" alt="card image" className="card-image" />
          <p>Card 4 description goes here</p>
        </div>
        <div className="card-footer">
          <button className="card-button">Button 4</button>
        </div>
      </div>
    </div>
  );
}

export default Communicate;
