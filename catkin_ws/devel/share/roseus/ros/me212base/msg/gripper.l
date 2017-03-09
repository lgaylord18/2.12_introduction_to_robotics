;; Auto-generated. Do not edit!


(when (boundp 'me212base::gripper)
  (if (not (find-package "ME212BASE"))
    (make-package "ME212BASE"))
  (shadow 'gripper (find-package "ME212BASE")))
(unless (find-package "ME212BASE::GRIPPER")
  (make-package "ME212BASE::GRIPPER"))

(in-package "ROS")
;;//! \htmlinclude gripper.msg.html


(defclass me212base::gripper
  :super ros::object
  :slots (_task ))

(defmethod me212base::gripper
  (:init
   (&key
    ((:task __task) 0)
    )
   (send-super :init)
   (setq _task (round __task))
   self)
  (:task
   (&optional __task)
   (if __task (setq _task __task)) _task)
  (:serialization-length
   ()
   (+
    ;; int16 _task
    2
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int16 _task
       (write-word _task s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int16 _task
     (setq _task (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;;
   self)
  )

(setf (get me212base::gripper :md5sum-) "4a46e74c396fe49dcc327f0e08dbcb98")
(setf (get me212base::gripper :datatype-) "me212base/gripper")
(setf (get me212base::gripper :definition-)
      "int16 task

")



(provide :me212base/gripper "4a46e74c396fe49dcc327f0e08dbcb98")


