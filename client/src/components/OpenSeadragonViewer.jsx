import React from 'react';
import { useEffect, useState } from "react";
import OpenSeaDragon from "openseadragon";
import '../styles/style.css'

const OpenSeadragonViewer = ({image}) => {

    const [viewer, setViewer] = useState(null);

    const initOpenseadragon = () => {
        viewer && viewer.destroy()
        setViewer(
            OpenSeaDragon({
                id: "openseadragon",
                prefixUrl: "openseadragon-images/",
                tileSources: `http://localhost:8000/${image}.dzi`,
                zoomPerScroll: 1.2,
                showNavigator: true,
            })
        );
    };

    useEffect(() => {
        console.log(image)
        if (image !== null){
            initOpenseadragon()
        }
    },[image]);
    
    return (
        <div id="openseadragon"> 
        
        </div> 
    );
}

export default OpenSeadragonViewer;


