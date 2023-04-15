import React from 'react';
import {useState, useEffect} from 'react'
import * as Annotorious from '@recogito/annotorious-openseadragon';
import '@recogito/annotorious-openseadragon/dist/annotorious.min.css';
import { useSelector } from 'react-redux';

const Drawer = () => {
    const [anno, setAnno] = useState(null)
    const viewer = useSelector(state => state.viewer)

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
        if (viewer) {
            initializeAnnotations(viewer)
        }
    }, [viewer]);

    return (
        <div>
            
        </div>
    );
}

export default Drawer;
