
(cl:in-package :asdf)

(defsystem "me212cv-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "DetectObject" :depends-on ("_package_DetectObject"))
    (:file "_package_DetectObject" :depends-on ("_package"))
  ))