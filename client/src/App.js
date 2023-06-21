import React from "react";
import OpenSeadragonViewer from "./components/OpenSeadragonViewer";
import UploadImage from "./components/UploadImage"
import Drawer from "./components/Drawer";

function App() {
    return (
        <div id="main-page">
            <OpenSeadragonViewer/>
            <UploadImage/>
            <Drawer></Drawer>
        </div> 
    );
}

export default App;
