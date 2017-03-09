// Auto-generated. Do not edit!

// (in-package me212cv.srv)


"use strict";

let _serializer = require('../base_serialize.js');
let _deserializer = require('../base_deserialize.js');
let _finder = require('../find.js');

//-----------------------------------------------------------


//-----------------------------------------------------------

class DetectObjectRequest {
  constructor() {
  }

  static serialize(obj, bufferInfo) {
    // Serializes a message object of type DetectObjectRequest
    return bufferInfo;
  }

  static deserialize(buffer) {
    //deserializes a message object of type DetectObjectRequest
    let tmp;
    let len;
    let data = new DetectObjectRequest();
    return {
      data: data,
      buffer: buffer
    }
  }

  static datatype() {
    // Returns string type for a service object
    return 'me212cv/DetectObjectRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'd41d8cd98f00b204e9800998ecf8427e';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    
    `;
  }

};

class DetectObjectResponse {
  constructor() {
    this.x = 0.0;
    this.y = 0.0;
    this.z = 0.0;
  }

  static serialize(obj, bufferInfo) {
    // Serializes a message object of type DetectObjectResponse
    // Serialize message field [x]
    bufferInfo = _serializer.float32(obj.x, bufferInfo);
    // Serialize message field [y]
    bufferInfo = _serializer.float32(obj.y, bufferInfo);
    // Serialize message field [z]
    bufferInfo = _serializer.float32(obj.z, bufferInfo);
    return bufferInfo;
  }

  static deserialize(buffer) {
    //deserializes a message object of type DetectObjectResponse
    let tmp;
    let len;
    let data = new DetectObjectResponse();
    // Deserialize message field [x]
    tmp = _deserializer.float32(buffer);
    data.x = tmp.data;
    buffer = tmp.buffer;
    // Deserialize message field [y]
    tmp = _deserializer.float32(buffer);
    data.y = tmp.data;
    buffer = tmp.buffer;
    // Deserialize message field [z]
    tmp = _deserializer.float32(buffer);
    data.z = tmp.data;
    buffer = tmp.buffer;
    return {
      data: data,
      buffer: buffer
    }
  }

  static datatype() {
    // Returns string type for a service object
    return 'me212cv/DetectObjectResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'cc153912f1453b708d221682bc23d9ac';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float32 x
    float32 y
    float32 z
    
    
    `;
  }

};

module.exports = {
  Request: DetectObjectRequest,
  Response: DetectObjectResponse
};
