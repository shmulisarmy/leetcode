package main


type Meeting struct{
	start_time int
	end_time int
}


func canAttendMeeting(target int) bool {
	var meetings  = []Meeting{{0,2}, {3,5}, {4, 15}, {6, 10}, {13, 16}}
	var target_time = 3
	for index = 1; index <= len(meetings)-1;  index++ {
		var time_between_meetings int = meetings[index].start_time - meetings[index-1]
		if time_between_meetings >= target_time {
			return true
		}
	}
	return false
}



func main() string|bool{
	print(canAttendMeeting(3))
	print(canAttendMeeting(1))
	print(canAttendMeeting(4))
	
}