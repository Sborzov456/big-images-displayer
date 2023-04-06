
import React, { Component } from 'react';
import OpenSeaDragon from "openseadragon"

class OSDClass extends Component {
    constructor(props) {
        super(props)
        this.state = {viewer: null}
    }

    componentWillMount() {
        this.setState(
            OpenSeaDragon({
                id: "openSeaDragon",
                prefixUrl: "openseadragon-images/",
                tileSources: 'http://localhost:8000/23-168-001.svs.dzi'
        }))
    }

    render() {
        return (
            <div id="openSeaDragon" style={{ height: "800px", width: "1200px" }}> 
            
            </div>
        );
    }
}

export default OSDClass;
