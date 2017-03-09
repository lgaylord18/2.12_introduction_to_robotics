;; Auto-generated. Do not edit!


(when (boundp 'me212cv::DetectObject)
  (if (not (find-package "ME212CV"))
    (make-package "ME212CV"))
  (shadow 'DetectObject (find-package "ME212CV")))
(unless (find-package "ME212CV::DETECTOBJECT")
  (make-package "ME212CV::DETECTOBJECT"))
(unless (find-package "ME212CV::DETECTOBJECTREQUEST")
  (make-package "ME212CV::DETECTOBJECTREQUEST"))
(unless (find-package "ME212CV::DETECTOBJECTRESPONSE")
  (make-package "ME212CV::DETECTOBJECTRESPONSE"))

(in-package "ROS")





(defclass me212cv::DetectObjectRequest
  :super ros::object
  :slots ())

(defmethod me212cv::DetectObjectRequest
  (:init
   (&key
    )
   (send-super :init)
   self)
  (:serialization-length
   ()
   (+
    0
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;;
   self)
  )

(defclass me212cv::DetectObjectResponse
  :super ros::object
  :slots (_x _y _z ))

(defmethod me212cv::DetectObjectResponse
  (:init
   (&key
    ((:x __x) 0.0)
    ((:y __y) 0.0)
    ((:z __z) 0.0)
    )
   (send-super :init)
   (setq _x (float __x))
   (setq _y (float __y))
   (setq _z (float __z))
   self)
  (:x
   (&optional __x)
   (if __x (setq _x __x)) _x)
  (:y
   (&optional __y)
   (if __y (setq _y __y)) _y)
  (:z
   (&optional __z)
   (if __z (setq _z __z)) _z)
  (:serialization-length
   ()
   (+
    ;; float32 _x
    4
    ;; float32 _y
    4
    ;; float32 _z
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _x
       (sys::poke _x (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _y
       (sys::poke _y (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _z
       (sys::poke _z (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _x
     (setq _x (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _y
     (setq _y (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _z
     (setq _z (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(defclass me212cv::DetectObject
  :super ros::object
  :slots ())

(setf (get me212cv::DetectObject :md5sum-) "cc153912f1453b708d221682bc23d9ac")
(setf (get me212cv::DetectObject :datatype-) "me212cv/DetectObject")
(setf (get me212cv::DetectObject :request) me212cv::DetectObjectRequest)
(setf (get me212cv::DetectObject :response) me212cv::DetectObjectResponse)

(defmethod me212cv::DetectObjectRequest
  (:response () (instance me212cv::DetectObjectResponse :init)))

(setf (get me212cv::DetectObjectRequest :md5sum-) "cc153912f1453b708d221682bc23d9ac")
(setf (get me212cv::DetectObjectRequest :datatype-) "me212cv/DetectObjectRequest")
(setf (get me212cv::DetectObjectRequest :definition-)
      "---
float32 x
float32 y
float32 z

")

(setf (get me212cv::DetectObjectResponse :md5sum-) "cc153912f1453b708d221682bc23d9ac")
(setf (get me212cv::DetectObjectResponse :datatype-) "me212cv/DetectObjectResponse")
(setf (get me212cv::DetectObjectResponse :definition-)
      "---
float32 x
float32 y
float32 z

")



(provide :me212cv/DetectObject "cc153912f1453b708d221682bc23d9ac")


