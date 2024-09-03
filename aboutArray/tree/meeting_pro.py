# 会议问题 给出几个会议的开始时间和结束时间 给出最优的会议安排
import heapq

import heapq


class Meeting:
    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time

    def __lt__(self, other):
        # 实现小于比较，确保堆中元素按结束时间升序排列
        return self.end_time < other.end_time

    def __repr__(self):
        return f"Meeting({self.start_time}, {self.end_time})"


def scheduling_meetings(off_duty_time, meetings):
    # 假设 meetings 是一个包含 (start_time, end_time) 元组的列表
    meetings_list = [Meeting(start, end) for start, end in meetings]
    heapq.heapify(meetings_list)
    result = []
    now_time = -1

    while meetings_list:
        current_meeting = heapq.heappop(meetings_list)
        if current_meeting.start_time >= now_time:
            result.append(current_meeting)
            now_time = current_meeting.end_time
            # 更新 end_time，这里假设 end_time 是一个全局结束时间
            if current_meeting.end_time < off_duty_time:
                off_duty_time = current_meeting.end_time

    return result


# 示例使用
meetings = [(1, 3), (2, 4), (3, 5), (6, 7)]
end_time = 8
scheduled = scheduling_meetings(end_time, meetings)
for m in scheduled:
    print(m)
