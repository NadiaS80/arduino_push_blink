// C++ code

void setup() {
   pinMode(13, OUTPUT); // объявляем пин 13 как выход
   pinMode(2, INPUT); // пин 2 как вход
}


int on_off = 0;
int last_state = 0;
int current_state = 0;

void loop() {
  if (digitalRead(2) == HIGH){
    current_state = 1;}
  else if (digitalRead(2) == LOW){
    current_state = 0;};
  
  if (current_state == 1 and last_state == 0){
    if (on_off == 0){
      digitalWrite(13, HIGH);
      on_off = 1;}
    else if (on_off == 1){
      digitalWrite(13, LOW);
      on_off = 0;};
  };
  
  last_state = current_state;

}