; Auto-generated. Do not edit!


(cl:in-package me212base-msg)


;//! \htmlinclude gripper.msg.html

(cl:defclass <gripper> (roslisp-msg-protocol:ros-message)
  ((task
    :reader task
    :initarg :task
    :type cl:fixnum
    :initform 0))
)

(cl:defclass gripper (<gripper>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <gripper>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'gripper)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name me212base-msg:<gripper> is deprecated: use me212base-msg:gripper instead.")))

(cl:ensure-generic-function 'task-val :lambda-list '(m))
(cl:defmethod task-val ((m <gripper>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader me212base-msg:task-val is deprecated.  Use me212base-msg:task instead.")
  (task m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <gripper>) ostream)
  "Serializes a message object of type '<gripper>"
  (cl:let* ((signed (cl:slot-value msg 'task)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <gripper>) istream)
  "Deserializes a message object of type '<gripper>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'task) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<gripper>)))
  "Returns string type for a message object of type '<gripper>"
  "me212base/gripper")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'gripper)))
  "Returns string type for a message object of type 'gripper"
  "me212base/gripper")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<gripper>)))
  "Returns md5sum for a message object of type '<gripper>"
  "4a46e74c396fe49dcc327f0e08dbcb98")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'gripper)))
  "Returns md5sum for a message object of type 'gripper"
  "4a46e74c396fe49dcc327f0e08dbcb98")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<gripper>)))
  "Returns full string definition for message of type '<gripper>"
  (cl:format cl:nil "int16 task~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'gripper)))
  "Returns full string definition for message of type 'gripper"
  (cl:format cl:nil "int16 task~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <gripper>))
  (cl:+ 0
     2
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <gripper>))
  "Converts a ROS message object to a list"
  (cl:list 'gripper
    (cl:cons ':task (task msg))
))
