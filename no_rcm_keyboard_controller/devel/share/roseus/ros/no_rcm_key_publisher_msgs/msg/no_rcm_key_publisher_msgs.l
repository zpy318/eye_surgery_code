;; Auto-generated. Do not edit!


(when (boundp 'no_rcm_key_publisher_msgs::no_rcm_key_publisher_msgs)
  (if (not (find-package "NO_RCM_KEY_PUBLISHER_MSGS"))
    (make-package "NO_RCM_KEY_PUBLISHER_MSGS"))
  (shadow 'no_rcm_key_publisher_msgs (find-package "NO_RCM_KEY_PUBLISHER_MSGS")))
(unless (find-package "NO_RCM_KEY_PUBLISHER_MSGS::NO_RCM_KEY_PUBLISHER_MSGS")
  (make-package "NO_RCM_KEY_PUBLISHER_MSGS::NO_RCM_KEY_PUBLISHER_MSGS"))

(in-package "ROS")
;;//! \htmlinclude no_rcm_key_publisher_msgs.msg.html


(defclass no_rcm_key_publisher_msgs::no_rcm_key_publisher_msgs
  :super ros::object
  :slots (_move_left _move_right _move_up _move_down _move_upward _move_downward _move_forward _move_backward _move_angle_insertion _move_angle_retraction _large_gain _small_gain _small_push ))

(defmethod no_rcm_key_publisher_msgs::no_rcm_key_publisher_msgs
  (:init
   (&key
    ((:move_left __move_left) nil)
    ((:move_right __move_right) nil)
    ((:move_up __move_up) nil)
    ((:move_down __move_down) nil)
    ((:move_upward __move_upward) nil)
    ((:move_downward __move_downward) nil)
    ((:move_forward __move_forward) nil)
    ((:move_backward __move_backward) nil)
    ((:move_angle_insertion __move_angle_insertion) nil)
    ((:move_angle_retraction __move_angle_retraction) nil)
    ((:large_gain __large_gain) nil)
    ((:small_gain __small_gain) nil)
    ((:small_push __small_push) nil)
    )
   (send-super :init)
   (setq _move_left __move_left)
   (setq _move_right __move_right)
   (setq _move_up __move_up)
   (setq _move_down __move_down)
   (setq _move_upward __move_upward)
   (setq _move_downward __move_downward)
   (setq _move_forward __move_forward)
   (setq _move_backward __move_backward)
   (setq _move_angle_insertion __move_angle_insertion)
   (setq _move_angle_retraction __move_angle_retraction)
   (setq _large_gain __large_gain)
   (setq _small_gain __small_gain)
   (setq _small_push __small_push)
   self)
  (:move_left
   (&optional __move_left)
   (if __move_left (setq _move_left __move_left)) _move_left)
  (:move_right
   (&optional __move_right)
   (if __move_right (setq _move_right __move_right)) _move_right)
  (:move_up
   (&optional __move_up)
   (if __move_up (setq _move_up __move_up)) _move_up)
  (:move_down
   (&optional __move_down)
   (if __move_down (setq _move_down __move_down)) _move_down)
  (:move_upward
   (&optional __move_upward)
   (if __move_upward (setq _move_upward __move_upward)) _move_upward)
  (:move_downward
   (&optional __move_downward)
   (if __move_downward (setq _move_downward __move_downward)) _move_downward)
  (:move_forward
   (&optional __move_forward)
   (if __move_forward (setq _move_forward __move_forward)) _move_forward)
  (:move_backward
   (&optional __move_backward)
   (if __move_backward (setq _move_backward __move_backward)) _move_backward)
  (:move_angle_insertion
   (&optional __move_angle_insertion)
   (if __move_angle_insertion (setq _move_angle_insertion __move_angle_insertion)) _move_angle_insertion)
  (:move_angle_retraction
   (&optional __move_angle_retraction)
   (if __move_angle_retraction (setq _move_angle_retraction __move_angle_retraction)) _move_angle_retraction)
  (:large_gain
   (&optional __large_gain)
   (if __large_gain (setq _large_gain __large_gain)) _large_gain)
  (:small_gain
   (&optional __small_gain)
   (if __small_gain (setq _small_gain __small_gain)) _small_gain)
  (:small_push
   (&optional __small_push)
   (if __small_push (setq _small_push __small_push)) _small_push)
  (:serialization-length
   ()
   (+
    ;; bool _move_left
    1
    ;; bool _move_right
    1
    ;; bool _move_up
    1
    ;; bool _move_down
    1
    ;; bool _move_upward
    1
    ;; bool _move_downward
    1
    ;; bool _move_forward
    1
    ;; bool _move_backward
    1
    ;; bool _move_angle_insertion
    1
    ;; bool _move_angle_retraction
    1
    ;; bool _large_gain
    1
    ;; bool _small_gain
    1
    ;; bool _small_push
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _move_left
       (if _move_left (write-byte -1 s) (write-byte 0 s))
     ;; bool _move_right
       (if _move_right (write-byte -1 s) (write-byte 0 s))
     ;; bool _move_up
       (if _move_up (write-byte -1 s) (write-byte 0 s))
     ;; bool _move_down
       (if _move_down (write-byte -1 s) (write-byte 0 s))
     ;; bool _move_upward
       (if _move_upward (write-byte -1 s) (write-byte 0 s))
     ;; bool _move_downward
       (if _move_downward (write-byte -1 s) (write-byte 0 s))
     ;; bool _move_forward
       (if _move_forward (write-byte -1 s) (write-byte 0 s))
     ;; bool _move_backward
       (if _move_backward (write-byte -1 s) (write-byte 0 s))
     ;; bool _move_angle_insertion
       (if _move_angle_insertion (write-byte -1 s) (write-byte 0 s))
     ;; bool _move_angle_retraction
       (if _move_angle_retraction (write-byte -1 s) (write-byte 0 s))
     ;; bool _large_gain
       (if _large_gain (write-byte -1 s) (write-byte 0 s))
     ;; bool _small_gain
       (if _small_gain (write-byte -1 s) (write-byte 0 s))
     ;; bool _small_push
       (if _small_push (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _move_left
     (setq _move_left (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _move_right
     (setq _move_right (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _move_up
     (setq _move_up (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _move_down
     (setq _move_down (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _move_upward
     (setq _move_upward (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _move_downward
     (setq _move_downward (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _move_forward
     (setq _move_forward (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _move_backward
     (setq _move_backward (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _move_angle_insertion
     (setq _move_angle_insertion (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _move_angle_retraction
     (setq _move_angle_retraction (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _large_gain
     (setq _large_gain (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _small_gain
     (setq _small_gain (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _small_push
     (setq _small_push (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(setf (get no_rcm_key_publisher_msgs::no_rcm_key_publisher_msgs :md5sum-) "c153bb0a32a052ad0d10173dacb72523")
(setf (get no_rcm_key_publisher_msgs::no_rcm_key_publisher_msgs :datatype-) "no_rcm_key_publisher_msgs/no_rcm_key_publisher_msgs")
(setf (get no_rcm_key_publisher_msgs::no_rcm_key_publisher_msgs :definition-)
      "bool move_left
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

")



(provide :no_rcm_key_publisher_msgs/no_rcm_key_publisher_msgs "c153bb0a32a052ad0d10173dacb72523")


