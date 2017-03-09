
(cl:in-package :asdf)

(defsystem "me212base-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "WheelVelCmd" :depends-on ("_package_WheelVelCmd"))
    (:file "_package_WheelVelCmd" :depends-on ("_package"))
    (:file "gripper" :depends-on ("_package_gripper"))
    (:file "_package_gripper" :depends-on ("_package"))
  ))