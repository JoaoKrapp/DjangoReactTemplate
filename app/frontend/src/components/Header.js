import React, { Component, useContext } from "react";
import { Link } from 'react-router-dom';

import AuthContext from "./context/AuthContext";

const Header = () => {

  let { logoutUser } = useContext(AuthContext);
  let { user } = useContext(AuthContext)

  let links;

  if (user == null) {
    links = (
      <ul>
			<li><Link to="/">Home</Link></li>
            <li><Link to="/login">Login</Link></li>
      </ul>
	  )
  }else {
	links = (
		<ul>
				<li><Link to="/">Home</Link></li>
				<li><Link to='/login' onClick={logoutUser}>Logout</Link></li>
		</ul>
	)
  }

  return (
    <div>
        { links }
    </div>
  )
}

export default Header