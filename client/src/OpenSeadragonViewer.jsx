import React from 'react';
import { useEffect, useState } from "react";
import OpenSeaDragon from "openseadragon";
import './styles/style.css'

const OpenSeadragonViewer = () => {

    const [viewer, setViewer] = useState(null);

    const initOpenseadragon = () => {
        setViewer(
            OpenSeaDragon({
                id: "openSeaDragon",
                prefixUrl: "openseadragon-images/",
                tileSources: 'http://localhost:8000/23-168-001.svs.dzi',
                zoomPerScroll: 1.2,
                showNavigator: true,
            })
        );
    };

    useEffect(() => initOpenseadragon, []);

    

    return (
        <div>
            <div id="openSeaDragon" style={{marginTop: 50, marginLeft: "auto", marginRight: "auto"}}> </div>
        </div>
        
    );
}

export default OpenSeadragonViewer;


