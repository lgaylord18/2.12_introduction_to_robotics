; Auto-generated. Do not edit!


(cl:in-package me212cv-srv)


;//! \htmlinclude DetectObject-request.msg.html

(cl:defclass <DetectObject-request> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass DetectObject-request (<DetectObject-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <DetectObject-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'DetectObject-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name me212cv-srv:<DetectObject-request> is deprecated: use me212cv-srv:DetectObject-request instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <DetectObject-request>) ostream)
  "Serializes a message object of type '<DetectObject-request>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <DetectObject-request>) istream)
  "Deserializes a message object of type '<DetectObject-request>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<DetectObject-request>)))
  "Returns string type for a service object of type '<DetectObject-request>"
  "me212cv/DetectObjectRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'DetectObject-request)))
  "Returns string type for a service object of type 'DetectObject-request"
  "me212cv/DetectObjectRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<DetectObject-request>)))
  "Returns md5sum for a message object of type '<DetectObject-request>"
  "cc153912f1453b708d221682bc23d9ac")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'DetectObject-request)))
  "Returns md5sum for a message object of type 'DetectObject-request"
  "cc153912f1453b708d221682bc23d9ac")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<DetectObject-request>)))
  "Returns full string definition for message of type '<DetectObject-request>"
  (cl:format cl:nil "~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'DetectObject-request)))
  "Returns full string definition for message of type 'DetectObject-request"
  (cl:format cl:nil "~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <DetectObject-request>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <DetectObject-request>))
  "Converts a ROS message object to a list"
  (cl:list 'DetectObject-request
))
;//! \htmlinclude DetectObject-response.msg.html

(cl:defclass <DetectObject-response> (roslisp-msg-protocol:ros-message)
  ((x
    :reader x
    :initarg :x
    :type cl:float
    :initform 0.0)
   (y
    :reader y
    :initarg :y
    :type cl:float
    :initform 0.0)
   (z
    :reader z
    :initarg :z
    :type cl:float
    :initform 0.0))
)

(cl:defclass DetectObject-response (<DetectObject-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <DetectObject-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'DetectObject-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name me212cv-srv:<DetectObject-response> is deprecated: use me212cv-srv:DetectObject-response instead.")))

(cl:ensure-generic-function 'x-val :lambda-list '(m))
(cl:defmethod x-val ((m <DetectObject-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader me212cv-srv:x-val is deprecated.  Use me212cv-srv:x instead.")
  (x m))

(cl:ensure-generic-function 'y-val :lambda-list '(m))
(cl:defmethod y-val ((m <DetectObject-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader me212cv-srv:y-val is deprecated.  Use me212cv-srv:y instead.")
  (y m))

(cl:ensure-generic-function 'z-val :lambda-list '(m))
(cl:defmethod z-val ((m <DetectObject-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader me212cv-srv:z-val is deprecated.  Use me212cv-srv:z instead.")
  (z m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <DetectObject-response>) ostream)
  "Serializes a message object of type '<DetectObject-response>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'x))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'y))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'z))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <DetectObject-response>) istream)
  "Deserializes a message object of type '<DetectObject-response>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'x) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'y) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'z) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<DetectObject-response>)))
  "Returns string type for a service object of type '<DetectObject-response>"
  "me212cv/DetectObjectResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'DetectObject-response)))
  "Returns string type for a service object of type 'DetectObject-response"
  "me212cv/DetectObjectResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<DetectObject-response>)))
  "Returns md5sum for a message object of type '<DetectObject-response>"
  "cc153912f1453b708d221682bc23d9ac")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'DetectObject-response)))
  "Returns md5sum for a message object of type 'DetectObject-response"
  "cc153912f1453b708d221682bc23d9ac")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<DetectObject-response>)))
  "Returns full string definition for message of type '<DetectObject-response>"
  (cl:format cl:nil "float32 x~%float32 y~%float32 z~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'DetectObject-response)))
  "Returns full string definition for message of type 'DetectObject-response"
  (cl:format cl:nil "float32 x~%float32 y~%float32 z~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <DetectObject-response>))
  (cl:+ 0
     4
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <DetectObject-response>))
  "Converts a ROS message object to a list"
  (cl:list 'DetectObject-response
    (cl:cons ':x (x msg))
    (cl:cons ':y (y msg))
    (cl:cons ':z (z msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'DetectObject)))
  'DetectObject-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'DetectObject)))
  'DetectObject-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'DetectObject)))
  "Returns string type for a service object of type '<DetectObject>"
  "me212cv/DetectObject")