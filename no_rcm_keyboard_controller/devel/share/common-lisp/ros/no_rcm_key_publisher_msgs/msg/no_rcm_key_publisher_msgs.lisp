; Auto-generated. Do not edit!


(cl:in-package no_rcm_key_publisher_msgs-msg)


;//! \htmlinclude no_rcm_key_publisher_msgs.msg.html

(cl:defclass <no_rcm_key_publisher_msgs> (roslisp-msg-protocol:ros-message)
  ((move_left
    :reader move_left
    :initarg :move_left
    :type cl:boolean
    :initform cl:nil)
   (move_right
    :reader move_right
    :initarg :move_right
    :type cl:boolean
    :initform cl:nil)
   (move_up
    :reader move_up
    :initarg :move_up
    :type cl:boolean
    :initform cl:nil)
   (move_down
    :reader move_down
    :initarg :move_down
    :type cl:boolean
    :initform cl:nil)
   (move_upward
    :reader move_upward
    :initarg :move_upward
    :type cl:boolean
    :initform cl:nil)
   (move_downward
    :reader move_downward
    :initarg :move_downward
    :type cl:boolean
    :initform cl:nil)
   (move_forward
    :reader move_forward
    :initarg :move_forward
    :type cl:boolean
    :initform cl:nil)
   (move_backward
    :reader move_backward
    :initarg :move_backward
    :type cl:boolean
    :initform cl:nil)
   (move_angle_insertion
    :reader move_angle_insertion
    :initarg :move_angle_insertion
    :type cl:boolean
    :initform cl:nil)
   (move_angle_retraction
    :reader move_angle_retraction
    :initarg :move_angle_retraction
    :type cl:boolean
    :initform cl:nil)
   (large_gain
    :reader large_gain
    :initarg :large_gain
    :type cl:boolean
    :initform cl:nil)
   (small_gain
    :reader small_gain
    :initarg :small_gain
    :type cl:boolean
    :initform cl:nil)
   (small_push
    :reader small_push
    :initarg :small_push
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass no_rcm_key_publisher_msgs (<no_rcm_key_publisher_msgs>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <no_rcm_key_publisher_msgs>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'no_rcm_key_publisher_msgs)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name no_rcm_key_publisher_msgs-msg:<no_rcm_key_publisher_msgs> is deprecated: use no_rcm_key_publisher_msgs-msg:no_rcm_key_publisher_msgs instead.")))

(cl:ensure-generic-function 'move_left-val :lambda-list '(m))
(cl:defmethod move_left-val ((m <no_rcm_key_publisher_msgs>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader no_rcm_key_publisher_msgs-msg:move_left-val is deprecated.  Use no_rcm_key_publisher_msgs-msg:move_left instead.")
  (move_left m))

(cl:ensure-generic-function 'move_right-val :lambda-list '(m))
(cl:defmethod move_right-val ((m <no_rcm_key_publisher_msgs>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader no_rcm_key_publisher_msgs-msg:move_right-val is deprecated.  Use no_rcm_key_publisher_msgs-msg:move_right instead.")
  (move_right m))

(cl:ensure-generic-function 'move_up-val :lambda-list '(m))
(cl:defmethod move_up-val ((m <no_rcm_key_publisher_msgs>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader no_rcm_key_publisher_msgs-msg:move_up-val is deprecated.  Use no_rcm_key_publisher_msgs-msg:move_up instead.")
  (move_up m))

(cl:ensure-generic-function 'move_down-val :lambda-list '(m))
(cl:defmethod move_down-val ((m <no_rcm_key_publisher_msgs>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader no_rcm_key_publisher_msgs-msg:move_down-val is deprecated.  Use no_rcm_key_publisher_msgs-msg:move_down instead.")
  (move_down m))

(cl:ensure-generic-function 'move_upward-val :lambda-list '(m))
(cl:defmethod move_upward-val ((m <no_rcm_key_publisher_msgs>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader no_rcm_key_publisher_msgs-msg:move_upward-val is deprecated.  Use no_rcm_key_publisher_msgs-msg:move_upward instead.")
  (move_upward m))

(cl:ensure-generic-function 'move_downward-val :lambda-list '(m))
(cl:defmethod move_downward-val ((m <no_rcm_key_publisher_msgs>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader no_rcm_key_publisher_msgs-msg:move_downward-val is deprecated.  Use no_rcm_key_publisher_msgs-msg:move_downward instead.")
  (move_downward m))

(cl:ensure-generic-function 'move_forward-val :lambda-list '(m))
(cl:defmethod move_forward-val ((m <no_rcm_key_publisher_msgs>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader no_rcm_key_publisher_msgs-msg:move_forward-val is deprecated.  Use no_rcm_key_publisher_msgs-msg:move_forward instead.")
  (move_forward m))

(cl:ensure-generic-function 'move_backward-val :lambda-list '(m))
(cl:defmethod move_backward-val ((m <no_rcm_key_publisher_msgs>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader no_rcm_key_publisher_msgs-msg:move_backward-val is deprecated.  Use no_rcm_key_publisher_msgs-msg:move_backward instead.")
  (move_backward m))

(cl:ensure-generic-function 'move_angle_insertion-val :lambda-list '(m))
(cl:defmethod move_angle_insertion-val ((m <no_rcm_key_publisher_msgs>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader no_rcm_key_publisher_msgs-msg:move_angle_insertion-val is deprecated.  Use no_rcm_key_publisher_msgs-msg:move_angle_insertion instead.")
  (move_angle_insertion m))

(cl:ensure-generic-function 'move_angle_retraction-val :lambda-list '(m))
(cl:defmethod move_angle_retraction-val ((m <no_rcm_key_publisher_msgs>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader no_rcm_key_publisher_msgs-msg:move_angle_retraction-val is deprecated.  Use no_rcm_key_publisher_msgs-msg:move_angle_retraction instead.")
  (move_angle_retraction m))

(cl:ensure-generic-function 'large_gain-val :lambda-list '(m))
(cl:defmethod large_gain-val ((m <no_rcm_key_publisher_msgs>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader no_rcm_key_publisher_msgs-msg:large_gain-val is deprecated.  Use no_rcm_key_publisher_msgs-msg:large_gain instead.")
  (large_gain m))

(cl:ensure-generic-function 'small_gain-val :lambda-list '(m))
(cl:defmethod small_gain-val ((m <no_rcm_key_publisher_msgs>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader no_rcm_key_publisher_msgs-msg:small_gain-val is deprecated.  Use no_rcm_key_publisher_msgs-msg:small_gain instead.")
  (small_gain m))

(cl:ensure-generic-function 'small_push-val :lambda-list '(m))
(cl:defmethod small_push-val ((m <no_rcm_key_publisher_msgs>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader no_rcm_key_publisher_msgs-msg:small_push-val is deprecated.  Use no_rcm_key_publisher_msgs-msg:small_push instead.")
  (small_push m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <no_rcm_key_publisher_msgs>) ostream)
  "Serializes a message object of type '<no_rcm_key_publisher_msgs>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'move_left) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'move_right) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'move_up) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'move_down) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'move_upward) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'move_downward) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'move_forward) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'move_backward) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'move_angle_insertion) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'move_angle_retraction) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'large_gain) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'small_gain) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'small_push) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <no_rcm_key_publisher_msgs>) istream)
  "Deserializes a message object of type '<no_rcm_key_publisher_msgs>"
    (cl:setf (cl:slot-value msg 'move_left) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'move_right) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'move_up) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'move_down) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'move_upward) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'move_downward) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'move_forward) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'move_backward) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'move_angle_insertion) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'move_angle_retraction) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'large_gain) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'small_gain) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'small_push) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<no_rcm_key_publisher_msgs>)))
  "Returns string type for a message object of type '<no_rcm_key_publisher_msgs>"
  "no_rcm_key_publisher_msgs/no_rcm_key_publisher_msgs")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'no_rcm_key_publisher_msgs)))
  "Returns string type for a message object of type 'no_rcm_key_publisher_msgs"
  "no_rcm_key_publisher_msgs/no_rcm_key_publisher_msgs")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<no_rcm_key_publisher_msgs>)))
  "Returns md5sum for a message object of type '<no_rcm_key_publisher_msgs>"
  "c153bb0a32a052ad0d10173dacb72523")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'no_rcm_key_publisher_msgs)))
  "Returns md5sum for a message object of type 'no_rcm_key_publisher_msgs"
  "c153bb0a32a052ad0d10173dacb72523")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<no_rcm_key_publisher_msgs>)))
  "Returns full string definition for message of type '<no_rcm_key_publisher_msgs>"
  (cl:format cl:nil "bool move_left~%bool move_right~%bool move_up~%bool move_down~%bool move_upward~%bool move_downward~%bool move_forward~%bool move_backward~%bool move_angle_insertion~%bool move_angle_retraction~%bool large_gain~%bool small_gain~%bool small_push~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'no_rcm_key_publisher_msgs)))
  "Returns full string definition for message of type 'no_rcm_key_publisher_msgs"
  (cl:format cl:nil "bool move_left~%bool move_right~%bool move_up~%bool move_down~%bool move_upward~%bool move_downward~%bool move_forward~%bool move_backward~%bool move_angle_insertion~%bool move_angle_retraction~%bool large_gain~%bool small_gain~%bool small_push~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <no_rcm_key_publisher_msgs>))
  (cl:+ 0
     1
     1
     1
     1
     1
     1
     1
     1
     1
     1
     1
     1
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <no_rcm_key_publisher_msgs>))
  "Converts a ROS message object to a list"
  (cl:list 'no_rcm_key_publisher_msgs
    (cl:cons ':move_left (move_left msg))
    (cl:cons ':move_right (move_right msg))
    (cl:cons ':move_up (move_up msg))
    (cl:cons ':move_down (move_down msg))
    (cl:cons ':move_upward (move_upward msg))
    (cl:cons ':move_downward (move_downward msg))
    (cl:cons ':move_forward (move_forward msg))
    (cl:cons ':move_backward (move_backward msg))
    (cl:cons ':move_angle_insertion (move_angle_insertion msg))
    (cl:cons ':move_angle_retraction (move_angle_retraction msg))
    (cl:cons ':large_gain (large_gain msg))
    (cl:cons ':small_gain (small_gain msg))
    (cl:cons ':small_push (small_push msg))
))
