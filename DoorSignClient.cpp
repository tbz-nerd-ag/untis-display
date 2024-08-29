#include <GxEPD2_BW.h>                                // needs the GxEPD2 libary 
#include <Fonts/FreeSerifBold12pt7b.h>                // adds the text style

GxEPD2_BW<GxEPD2_420_GDEY042T81, GxEPD2_420_GDEY042T81::HEIGHT> display(GxEPD2_420_GDEY042T81(/*CS=D8*/ SS, /*DC=D3*/ 0, /*RST=D4*/ 2, /*BUSY=D2*/ 4)); // GDEY042T81, 400x300, SSD1683 (no inking)

void setup() 
{
    display.init();                         // initialis the E-paper Display
    display.setRotation(1);                 // sets the Rotaion to horizontily
    display.setFont(&FreeSerifBold12pt7b);  // sets the Text style as default
    display.setTextColor(GxEPD_BLACK);      // sets the Text color
    display.setFullWindow();                // tells the E-paper Display to use the hole Display
    updateScreen();                         // calls the updateScreen method
    display.hibernate();                    // set the Display to sleep mode 
}

void updateScreen()                         // set the default Display 
{
  display.firstPage();                      // saves the following as the first page
  do 
  {
    display.fillScreen(GxEPD_WHITE);        // sets the background to white
    display.setCursor(60, 70);              // sets the position of the Text
    display.print("Hello World");           // writes the Text
  }
  while (display.nextPage());               // finising the page
}

void loop() 
{
  
}
