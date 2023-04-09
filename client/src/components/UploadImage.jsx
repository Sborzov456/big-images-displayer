import React from 'react';
import Button from '@mui/material/Button';
import Stack from '@mui/material/Stack';

const SelectImage = ({sendImage}) => {

    const upload = (event) => {
        const file = event.target.files[0]
        const formData = new FormData()
        formData.append('image', file, file.name)

        fetch('http://localhost:8000/upload', {
            method: 'POST',
            "Content-Type": "multipart/form-data",
            body: formData
        })
        .then(response => response.text())
        .then(result => {
            sendImage(result)
        })
    }

    return (
        <Stack direction="row" alignItems="center" spacing={2} style={{margin: 20}}>
            <Button variant="contained" component="label">
                Upload
                <input onChange={upload} hidden multiple type="file"/>
            </Button>
        </Stack>
    );
}

export default SelectImage;
