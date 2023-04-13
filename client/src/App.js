import React from "react";
import {useState} from 'react'
import OpenSeadragonViewer from "./components/OpenSeadragonViewer";
import UploadImage from "./components/UploadImage"
import { Drawer } from "@mui/material";

function App() {
    const [image, setImage] = useState(null)

    const getImage = (image) => {
        setImage(image)
    }

    return (
        <div id="main-page">
            <OpenSeadragonViewer image={image}/>
            <UploadImage sendImage={getImage}/>
            <Drawer> </Drawer>
        </div> 
    );
}

export default App;
