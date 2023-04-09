import { useState} from "react";
import './Home.css';
import {Link} from "react-router-dom";
import Communicate from '../Communicate/Communicate';

function Home() {
  const [isActive, setActive] = useState(false);

  const handleSignUpClick = () => {
    setActive(true);
  };

  const handleSignInClick = () => {
    setActive(false);
  };


  return (
    <div class='form-cover'>
    <div className={`container ${isActive ? "right-panel-active" : ""}`} id="qwerty">
      <div className="form-container sign-up-container">
        <form>
          <h1>LOCAL</h1>
        
          {/* <span>Create an account</span>
          <input type="text" placeholder="Name" />
          <input type="email" placeholder="Email" />
          <input type="password" placeholder="Password" /> */}
          <button><Link to='/local' id="qwerty">Do this!</Link></button>
        </form>
      </div>
      <div className="form-container sign-in-container">
        <form>
          <h1>COMMUNICATE</h1>
          
          {/* <span>Already have account ? </span>
          <input type="email" placeholder="Email" />
          <input type="password" placeholder="Password" /> */}
          <button > <Link to='/Communicate' id="qwerty">Do this!</Link> </button>
        </form>
      </div>
      <div className="overlay-container">
        <div className="overlay">
          <div className="overlay-panel overlay-left">
            <h1>Covert</h1>
            <p>Rather use communication channels?</p>
            <button className="ghost" onClick={handleSignInClick} id="signIn">
              Go back to local!
            </button>
          </div>
          <div className="overlay-panel overlay-right">
            <h1>HIDING</h1>
            <p>Want to use local file system? </p>
            <button className="ghost" onClick={handleSignUpClick} id="signUp">
              Go to Local
            </button>
          </div>
        </div>
      </div>
    </div>
    </div>
  );
}

export default Home;