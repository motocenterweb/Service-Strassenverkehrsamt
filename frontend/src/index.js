import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import { Navigation } from './components';
import { Übersicht, Fahrzeuge, Fuehrerschein, StVO } from './views';


const root = ReactDOM.createRoot(document.getElementById('root'));
root.render((
  <Router>
    <Navigation />
    <Routes>
      <Route path="/" element={<Übersicht />} />
      <Route path="/Fahrzeuge" element={<Fahrzeuge />} />
      <Route path="/Fuehrerschein" element={<Fuehrerschein />} />
      <Route path="/StVO" element={<StVO />} />
    </Routes>
  </Router>
  )
);
