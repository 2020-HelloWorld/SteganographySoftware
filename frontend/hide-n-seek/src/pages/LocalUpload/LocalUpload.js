import React, { useState } from "react";
import styled, { keyframes } from "styled-components";

const fadeIn = keyframes`
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
`;

const slideInDown = keyframes`
  from {
    transform: translateY(-100%);
  }
  to {
    transform: translateY(0);
  }
`;

const FlexBox = styled.div`
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100vh;
`;

const UploadBox = styled.div`
  background-color: #eee;
  border-radius: 5px;
  padding: 20px;
  animation: ${fadeIn} 0.5s ease-in-out;
`;

const UploadInput = styled.input`
  font-size: 1.2rem;
  padding: 10px;
  margin-bottom: 10px;
`;

const UploadButton = styled.button`
  font-size: 1.2rem;
  padding: 10px 20px;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: all 0.3s ease-in-out;
  &:hover {
    background-color: #3e8e41;
  }
`;

const SuccessBox = styled.div`
  background-color: #3e8e41;
  border-radius: 5px;
  padding: 20px;
  animation: ${slideInDown} 0.5s ease-in-out;
`;

const SuccessText = styled.p`
  font-size: 1.2rem;
  color: white;
`;

const ErrorBox = styled.div`
  background-color: #f44336;
  border-radius: 5px;
  padding: 20px;
  animation: ${slideInDown} 0.5s ease-in-out;
`;

const ErrorText = styled.p`
  font-size: 1.2rem;
  color: white;
`;

const FileUploader = () => {
  const [file, setFile] = useState(null);
  const [uploadStatus, setUploadStatus] = useState(null);

  const handleFileUpload = e => {
    setFile(e.target.files[0]);
    setUploadStatus(null);
  };

  const handleUpload = () => {
    const formData = new FormData();
    formData.append("file", file);
    fetch("http://<IP /upload", {
      method: "POST",
      body: formData,
    })
      .then(response => {
        if (!response.ok) {
          throw new Error("Upload failed");
        }
        return response.json();
      })
      .then(data => {
        console.log("Upload successful");
        setUploadStatus("success");
      })
      .catch(error => {
        console.error(error);
        setUploadStatus("error");
      });
  };

  return (
    <FlexBox>
      {uploadStatus === "success" ? (
        <SuccessBox>
          <SuccessText>File uploaded successfully</SuccessText>
        </SuccessBox>
      ) : uploadStatus === "error" ? (
        <ErrorBox>
          <ErrorText>File upload failed</ErrorText>
        </ErrorBox>
      ) : (
        <UploadBox>
          <UploadInput type="file" onChange={handleFileUpload} />
          <UploadButton onClick={handleUpload}>Upload</UploadButton>
        </UploadBox>
      )}
    </FlexBox>
  );
};

export default FileUploader;
