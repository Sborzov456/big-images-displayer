import React from "react";
import {useState} from 'react'
import OpenSeadragonViewer from "./components/OpenSeadragonViewer";
import UploadImage from "./components/UploadImage"

function App() {
    const [image, setImage] = useState(null)

    const getImage = (image) => {
        setImage(image)
    }

    return (
        <div id="main-page">
            <OpenSeadragonViewer image={image}/>
            <UploadImage sendImage={getImage}/>
        </div> 
    );
}

export default App;
