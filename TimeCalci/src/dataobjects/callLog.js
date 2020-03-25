export default class CallLog {
  constructor(id, phoneNumber, prefix, type, duration, timestamp, dateTime) {
    this.id = id;
    this.phoneNumber = phoneNumber;
    this.prefix = prefix;
    this.type = type;
    this.duration = duration;
    this.timestamp = timestamp;
    this.dateTime = dateTime;
  }
}
