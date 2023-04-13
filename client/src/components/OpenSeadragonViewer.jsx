import React from 'react';
import { useEffect, useState } from "react";
import OpenSeaDragon from "openseadragon";
import '../styles/style.css'
import * as Annotorious from '@recogito/annotorious-openseadragon';
import '@recogito/annotorious-openseadragon/dist/annotorious.min.css';


const OpenSeadragonViewer = ({image}) => {

    const [viewer, setViewer] = useState(null);
    const [anno, setAnno] = useState(null)

    const initialize = () => {
        // init viewer
        const viewerState = initializeViewer()

        //init annotations
        initializeAnnotations(viewerState)
    };

    const initializeViewer = () => {
        viewer && viewer.destroy()
        const viewerState = OpenSeaDragon({
                id: "openseadragon",
                prefixUrl: "openseadragon-images/",
                tileSources: `http://localhost:8000/${image}.dzi`,
                showNavigator: true,
                animationTime: 0.5,
                blendTime: 0.1,
                constrainDuringPan: true,
                maxZoomPixelRatio: 2,
                minZoomLevel: 1,
                visibilityRatio: 1,
                zoomPerScroll: 1.2
            })
        setViewer(viewerState)
        return viewerState
    }

    const initializeAnnotations = (viewer) => {
        anno && anno.destroy()
        const annotateState = Annotorious(viewer, {formatter});
        annotateState.setDrawingTool('polygon')
        setAnno(annotateState)
    }

    const formatter = (annotation) => {
        return 'important'
    }

    useEffect(() => {
        if (image) {
            initialize()
        }
    },[image]);
    
    return (
        <div id="openseadragon"> </div> 
    );
}

export default OpenSeadragonViewer;


