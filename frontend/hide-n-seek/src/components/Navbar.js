import React from 'react'
import {Link} from "react-router-dom";
export default function Navbar() {
  return (
    <nav className='nav'>
        <Link to='/' className='site-title'>Site Name</Link>
        <ul>
            <li>
                <Link to='/Local'>Local</Link>
            </li>
            <li>
            <Link to='/Communicate'>Communicate</Link>
            </li>
        </ul>
    </nav>
  )
}