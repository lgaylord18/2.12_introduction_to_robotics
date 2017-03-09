// Auto-generated. Do not edit!

// (in-package me212base.msg)


"use strict";

let _serializer = require('../base_serialize.js');
let _deserializer = require('../base_deserialize.js');
let _finder = require('../find.js');

//-----------------------------------------------------------

class gripper {
  constructor() {
    this.task = 0;
  }

  static serialize(obj, bufferInfo) {
    // Serializes a message object of type gripper
    // Serialize message field [task]
    bufferInfo = _serializer.int16(obj.task, bufferInfo);
    return bufferInfo;
  }

  static deserialize(buffer) {
    //deserializes a message object of type gripper
    let tmp;
    let len;
    let data = new gripper();
    // Deserialize message field [task]
    tmp = _deserializer.int16(buffer);
    data.task = tmp.data;
    buffer = tmp.buffer;
    return {
      data: data,
      buffer: buffer
    }
  }

  static datatype() {
    // Returns string type for a message object
    return 'me212base/gripper';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '4a46e74c396fe49dcc327f0e08dbcb98';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int16 task
    
    `;
  }

};

module.exports = gripper;
