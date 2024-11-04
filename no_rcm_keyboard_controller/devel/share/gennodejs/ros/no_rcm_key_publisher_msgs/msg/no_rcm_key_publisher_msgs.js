// Auto-generated. Do not edit!

// (in-package no_rcm_key_publisher_msgs.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class no_rcm_key_publisher_msgs {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.move_left = null;
      this.move_right = null;
      this.move_up = null;
      this.move_down = null;
      this.move_upward = null;
      this.move_downward = null;
      this.move_forward = null;
      this.move_backward = null;
      this.move_angle_insertion = null;
      this.move_angle_retraction = null;
      this.large_gain = null;
      this.small_gain = null;
      this.small_push = null;
    }
    else {
      if (initObj.hasOwnProperty('move_left')) {
        this.move_left = initObj.move_left
      }
      else {
        this.move_left = false;
      }
      if (initObj.hasOwnProperty('move_right')) {
        this.move_right = initObj.move_right
      }
      else {
        this.move_right = false;
      }
      if (initObj.hasOwnProperty('move_up')) {
        this.move_up = initObj.move_up
      }
      else {
        this.move_up = false;
      }
      if (initObj.hasOwnProperty('move_down')) {
        this.move_down = initObj.move_down
      }
      else {
        this.move_down = false;
      }
      if (initObj.hasOwnProperty('move_upward')) {
        this.move_upward = initObj.move_upward
      }
      else {
        this.move_upward = false;
      }
      if (initObj.hasOwnProperty('move_downward')) {
        this.move_downward = initObj.move_downward
      }
      else {
        this.move_downward = false;
      }
      if (initObj.hasOwnProperty('move_forward')) {
        this.move_forward = initObj.move_forward
      }
      else {
        this.move_forward = false;
      }
      if (initObj.hasOwnProperty('move_backward')) {
        this.move_backward = initObj.move_backward
      }
      else {
        this.move_backward = false;
      }
      if (initObj.hasOwnProperty('move_angle_insertion')) {
        this.move_angle_insertion = initObj.move_angle_insertion
      }
      else {
        this.move_angle_insertion = false;
      }
      if (initObj.hasOwnProperty('move_angle_retraction')) {
        this.move_angle_retraction = initObj.move_angle_retraction
      }
      else {
        this.move_angle_retraction = false;
      }
      if (initObj.hasOwnProperty('large_gain')) {
        this.large_gain = initObj.large_gain
      }
      else {
        this.large_gain = false;
      }
      if (initObj.hasOwnProperty('small_gain')) {
        this.small_gain = initObj.small_gain
      }
      else {
        this.small_gain = false;
      }
      if (initObj.hasOwnProperty('small_push')) {
        this.small_push = initObj.small_push
      }
      else {
        this.small_push = false;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type no_rcm_key_publisher_msgs
    // Serialize message field [move_left]
    bufferOffset = _serializer.bool(obj.move_left, buffer, bufferOffset);
    // Serialize message field [move_right]
    bufferOffset = _serializer.bool(obj.move_right, buffer, bufferOffset);
    // Serialize message field [move_up]
    bufferOffset = _serializer.bool(obj.move_up, buffer, bufferOffset);
    // Serialize message field [move_down]
    bufferOffset = _serializer.bool(obj.move_down, buffer, bufferOffset);
    // Serialize message field [move_upward]
    bufferOffset = _serializer.bool(obj.move_upward, buffer, bufferOffset);
    // Serialize message field [move_downward]
    bufferOffset = _serializer.bool(obj.move_downward, buffer, bufferOffset);
    // Serialize message field [move_forward]
    bufferOffset = _serializer.bool(obj.move_forward, buffer, bufferOffset);
    // Serialize message field [move_backward]
    bufferOffset = _serializer.bool(obj.move_backward, buffer, bufferOffset);
    // Serialize message field [move_angle_insertion]
    bufferOffset = _serializer.bool(obj.move_angle_insertion, buffer, bufferOffset);
    // Serialize message field [move_angle_retraction]
    bufferOffset = _serializer.bool(obj.move_angle_retraction, buffer, bufferOffset);
    // Serialize message field [large_gain]
    bufferOffset = _serializer.bool(obj.large_gain, buffer, bufferOffset);
    // Serialize message field [small_gain]
    bufferOffset = _serializer.bool(obj.small_gain, buffer, bufferOffset);
    // Serialize message field [small_push]
    bufferOffset = _serializer.bool(obj.small_push, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type no_rcm_key_publisher_msgs
    let len;
    let data = new no_rcm_key_publisher_msgs(null);
    // Deserialize message field [move_left]
    data.move_left = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [move_right]
    data.move_right = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [move_up]
    data.move_up = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [move_down]
    data.move_down = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [move_upward]
    data.move_upward = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [move_downward]
    data.move_downward = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [move_forward]
    data.move_forward = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [move_backward]
    data.move_backward = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [move_angle_insertion]
    data.move_angle_insertion = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [move_angle_retraction]
    data.move_angle_retraction = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [large_gain]
    data.large_gain = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [small_gain]
    data.small_gain = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [small_push]
    data.small_push = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 13;
  }

  static datatype() {
    // Returns string type for a message object
    return 'no_rcm_key_publisher_msgs/no_rcm_key_publisher_msgs';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'c153bb0a32a052ad0d10173dacb72523';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    bool move_left
    bool move_right
    bool move_up
    bool move_down
    bool move_upward
    bool move_downward
    bool move_forward
    bool move_backward
    bool move_angle_insertion
    bool move_angle_retraction
    bool large_gain
    bool small_gain
    bool small_push
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new no_rcm_key_publisher_msgs(null);
    if (msg.move_left !== undefined) {
      resolved.move_left = msg.move_left;
    }
    else {
      resolved.move_left = false
    }

    if (msg.move_right !== undefined) {
      resolved.move_right = msg.move_right;
    }
    else {
      resolved.move_right = false
    }

    if (msg.move_up !== undefined) {
      resolved.move_up = msg.move_up;
    }
    else {
      resolved.move_up = false
    }

    if (msg.move_down !== undefined) {
      resolved.move_down = msg.move_down;
    }
    else {
      resolved.move_down = false
    }

    if (msg.move_upward !== undefined) {
      resolved.move_upward = msg.move_upward;
    }
    else {
      resolved.move_upward = false
    }

    if (msg.move_downward !== undefined) {
      resolved.move_downward = msg.move_downward;
    }
    else {
      resolved.move_downward = false
    }

    if (msg.move_forward !== undefined) {
      resolved.move_forward = msg.move_forward;
    }
    else {
      resolved.move_forward = false
    }

    if (msg.move_backward !== undefined) {
      resolved.move_backward = msg.move_backward;
    }
    else {
      resolved.move_backward = false
    }

    if (msg.move_angle_insertion !== undefined) {
      resolved.move_angle_insertion = msg.move_angle_insertion;
    }
    else {
      resolved.move_angle_insertion = false
    }

    if (msg.move_angle_retraction !== undefined) {
      resolved.move_angle_retraction = msg.move_angle_retraction;
    }
    else {
      resolved.move_angle_retraction = false
    }

    if (msg.large_gain !== undefined) {
      resolved.large_gain = msg.large_gain;
    }
    else {
      resolved.large_gain = false
    }

    if (msg.small_gain !== undefined) {
      resolved.small_gain = msg.small_gain;
    }
    else {
      resolved.small_gain = false
    }

    if (msg.small_push !== undefined) {
      resolved.small_push = msg.small_push;
    }
    else {
      resolved.small_push = false
    }

    return resolved;
    }
};

module.exports = no_rcm_key_publisher_msgs;
