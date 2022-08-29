import React, { Component } from "react";
import { render } from "react-dom";
import {
	BrowserRouter as Router,
	Routes,
	Route,
	Link,
	Redirect,
  } from "react-router-dom";

import { AuthProvider } from "./context/AuthContext";

// Import components

import PrivateRoute from "./utils/PrivateRoute";

import Homepage from "./Homepage";
import Login from "./Login";

import Header from "./Header";

function App() {
  return (
	<Router>
		<AuthProvider>
		<Header></Header>
			<Routes>
				{/* Private Routes */}
				<Route exact path='/' element={<PrivateRoute/>}>
					<Route exact path='/' element={<Homepage/>}/>
				</Route>

				{/* Public routes */}
				<Route exact path="/login" element={<Login/>}></Route>
				<Route exact path="/feed" element={<h1>Teste</h1>}></Route>
			</Routes>
		</AuthProvider>
	</Router>
  );
}

export default App;