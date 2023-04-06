import React from 'react';
import { useEffect, useState } from "react";
import OpenSeaDragon from "openseadragon";

const OpenSeadragonViewer = () => {

    const [viewer, setViewer] = useState(null);

    const InitOpenseadragon = () => {
        setViewer(
            OpenSeaDragon({
                id: "openSeaDragon",
                prefixUrl: "openseadragon-images/",
                tileSources: 'http://localhost:8000/23-168-001.svs.dzi'
            })
        );
    };

    useEffect(() => InitOpenseadragon, []);

    

    return (
        <div>
            <div id="openSeaDragon" style={{ height: "800px", width: "1200px" }}> </div>
            {/* <button onClick={() => {
                viewer.world.resetItams()
            }}> Clear </button> */}
        </div>
    );
}

export default OpenSeadragonViewer;


