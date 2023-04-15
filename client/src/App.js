import React from "react";
import {useState} from 'react'
import OpenSeadragonViewer from "./components/OpenSeadragonViewer";
import UploadImage from "./components/UploadImage"

function App() {
    const [image, setImage] = useState(null)

    return (
        <div id="main-page">
            <OpenSeadragonViewer/>
            <UploadImage/>
        </div> 
    );
}

export default App;
