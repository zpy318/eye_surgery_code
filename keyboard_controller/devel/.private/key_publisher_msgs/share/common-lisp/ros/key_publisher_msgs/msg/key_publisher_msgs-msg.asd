
(cl:in-package :asdf)

(defsystem "key_publisher_msgs-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "key_publisher_msgs" :depends-on ("_package_key_publisher_msgs"))
    (:file "_package_key_publisher_msgs" :depends-on ("_package"))
  ))