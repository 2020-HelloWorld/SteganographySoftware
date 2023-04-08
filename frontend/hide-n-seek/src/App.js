import logo from './logo.svg';
import './App.css';
import Navbar from './components/Navbar';
import Home from "./pages/Home/Home";
import Local from './pages/Local/Local';
import Communicate from './pages/Communicate/Communicate';
import LocalUpload from './pages/LocalUpload/LocalUpload';

import {Routes , Route,useNavigate} from "react-router-dom";

function App() {
  return (
    <>
    <div className='container'>
      <Routes>
        <Route path='/' element={<Home />} />
        <Route path='/local' element={<Local/>} />
        <Route path='/communicate' element={<Communicate />} />
        <Route path='/localupload' element={<LocalUpload />} />
      </Routes>
    </div></>
  );
}

export default App;
