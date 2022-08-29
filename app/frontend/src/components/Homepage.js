import React, { Component, useContext, useEffect, useState } from "react";
import '../style/Homepage.css'
import AuthContext from "./context/AuthContext";

// Developer components

import Header from "./Header";

function Homepage() {
	let {user, authToken} = useContext(AuthContext);

	let [notes, setNotes] = useState([])

	useEffect(() => {
		getNotes()
	}, [])

	let getNotes = async() => {
        let response = await fetch('http://127.0.0.1:8000/api/notes/', {
            method:'GET',
            headers:{
                'Content-Type':'application/json',
                'Authorization':'Bearer ' + String(authToken.access)
            }
        })
        let data = await response.json()

        if(response.status === 200){
            setNotes(data)
			
        }else if(response.statusText === 'Unauthorized'){
            logoutUser()
        }
        
    }

	return (
		<div>
			<h1 id="lmao">LMAO, {user && <b>Hello {user.username}</b>} </h1>

			<ul>
				{notes.map(note => (
                    <li key={note.id} >{note.body}</li>
                ))}
			</ul>
		</div>
	);
}

export default Homepage;