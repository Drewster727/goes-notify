# goes-notify

This app will simply parse json output from the interview scheduler for many of CBP's Trusted Traveler Programs, including Global Entry, NEXUS, SENTRI, US/Mexico FAST, and US/Canada FAST. You don't need to provide a login, it will simply check the available dates against your current interview date, then notify you if a better date can be locked in.

Based on the ge-cancellation-checker that originally utilized phantomjs to login as the user:
https://github.com/davidofwatkins/ge-cancellation-checker

# Getting started

- Clone the repo
- Enter required fields into `config.json`:
  - Look up your enrollment center in the list below
  - Enter your current interview date in Month name-Day-Year format. E.g., "December 10, 2017"

# Usage

Run the script with `python`: `python2 goes-notify.py`

If you're running this on a machine you'll be using while it's searching, you can set the `no-email` config setting and receive a local macOS notification when the script finds a new appointment.

With the `use_gmail` config setting, you can send yourself an email when an appointment is found. Note: if you have two-factor authentication enabled for your account, you'll need to [generate an app-specific password](https://myaccount.google.com/apppasswords) and add that to `config.json`.

If you would like to check multiple nearby locations at once you need to make copies the original file you just edited and change the location code on each config file. Then in seperate windows run each copy of the diffrent locations. If you set `enrollment_location_name` in the config file, the alert message will display this name, otherwise the `enrollment_location_id` will be displayed. 

# Using Docker

This is the easiest way. Install docker (any operating system). Just make a copy of the config.json file, update it accordingly, and then run the below command:

```
docker run -d -v /path/to/config.json:/app/config.json drewster727/goes-notify
```

----

# GOES center codes

The table below may not be complete. If you don't see your location, visit [this link](https://ttp.cbp.dhs.gov/schedulerapi/locations/?temporary=false&inviteOnly=false&operational=true&serviceName=Global%20Entry) for a current complete list; find your desired location; and use the 'id' field as the location code in your config file:

| ID    | Enrollment Center Name                                                                                                                |
|-------|---------------------------------------------------------------------------------------------------------------------------------------|
| 8040  | Albuquerque Enrollment Center - Albuquerque International Sunport 2200 Sunport Blvd SE   Albuquerque NM 87106                         |
| 6580  | American Express - New York - 0 UNAVAILABLE NEW YORK NY 99999 US                                                                      |
| 7540  | Anchorage Enrollment Center - Ted Stevens International Airport 4600 Postmark Drive RM NA 207 Anchorage                               |
| 5182  | Atlanta International Global Entry EC - 2600 Maynard H. Jackson Jr. Int'l Terminal Maynard H. Jackson Jr. Blvd.                       |
| 5200  | Atlanta Port Office Global Entry Enrollment Center - 157 Tradeport Drive Suite C Atlanta GA 30354 US                                  |
| 7820  | Austin-Bergstrom International Airport - 3600 Presidential Blvd. Austin-Bergstrom International Airport                               |
| 7940  | Baltimore Enrollment Center - Baltimore Washington Thurgood Marshall I Lower Level Door 18 Linthicum MD 21240                         |
| 13321 | Blaine Global Entry Enrollment Center - 8115 Birch Bay Square St. Suite 104 Blaine WA 98230 US                                        |
| 12161 | Boise Enrollment Center - 4655 S Enterprise Street Boise ID 83705 US                                                                  |
| 14221 | Boston- Tip O'Neill Federal Building - 10 Causeway Street Room 812 Boston MA 02222 US                                                 |
| 5441  | Boston-Logan Global Entry Enrollment Center - Logan International Airport Terminal E East Boston MA 02128                             |
| 5003  | Brownsville Enrollment Center - 3300 South Expressway 77 83 Veterans International Bridge - Los Tomates                               |
| 5022  | Buffalo-Ft. Erie Enrollment Center - 10 CENTRAL AVENUE FORT ERIE ON L2A1G6 CA                                                         |
| 5500  | Calais Enrollment Center - 3 Customs Street, Calais, MAINE 04619                                                                      |
| 5006  | Calexico Enrollment Center - 1699 E. Carr Rd PO BOX 632 Calexico CA 92231 US                                                          |
| 5030  | Calgary Enrollment Center - 2000 Airport Rd N.E. Calgary AB T2E6W5 CA                                                                 |
| 13801 | Champlain Global Entry Enrollment Center - 237 West Service Road Champlain NY 12919 US                                                |
| 14321 | Charlotte-Douglas - DOWNSTAIRS LOCATION - 5501 Charlotte-Douglas International Airport Josh Birmingham Parkway                        |
| 11981 | Chicago Field Office Enrollment Center - 610 Closed until further notice Closed until futher notice  Chicago                          |
| 5183  | Chicago O'Hare International Global Entry EC  - 10000 Bessie Coleman Drive Terminal 5 Lower Level Chicago                             |
| 7680  | Cincinnati Enrollment Center - 4243 Olympic Blvd. Suite. 210 Erlanger KY 41018 US                                                     |
| 9180  | Cleveland U.S. Customs and Border Protection - Customs & Border Protection 6747 Engle Road Middleburg Heights                         |
| 5300  | Dallas-Fort Worth Intl Airport Global Entry - DFW International Airport - Terminal D DFW Airport TX 75261                             |
| 14161 |  DBX-SF -                                                                                                                             |
| 14021 | DCL2017 - This is a private event.                                                                                                    |
| 6940  | Denver International Airport - 8400 Denver International Airport Pena Boulevard Denver CO 80249 US                                    |
| 5223  | Derby Line Enrollment Center - 84 Main Street Derby Line VT 08530 US                                                                  |
| 14421 | DESIGNTRAVEL2017 -                                                                                                                    |
| 5023  | Detroit Enrollment Center - 2810 WEST FORT STREET BUILDING B DETROIT MI 48226 US                                                      |
| 5320  | Detroit Metro Airport Global Entry - 601 Detroit North Terminal Rogell Dr. Suite 1271 Detroit MI 48242                                |
| 14281 |  DLGA GO EVENT -                                                                                                                      |
| 6920  |  Doha International Airport - Hamad International Airport Doha QA                                                                     |
| 8100  | Douglas Enrollment Center - 1012 G Avenue Suite 107 Douglas AZ 85607 US                                                               |
| 5032  | Edmonton Enrollment Center - 1000 Airport Road Edmonton International Airport Edmonton AB T9E0V3 CA                                   |
| 14361 | EGESBOS2017 -                                                                                                                         |
| 5005  | El Paso Enrollment Center - 797 S. Zaragoza Rd. Bldg.  A El Paso TX 79907 US                                                          |
| 14301 | EMRSN2017 -                                                                                                                           |
| 14381 | Fairbanks Enrollment Center - 6450 Airport Way - Suite 13 Room 1320A Fairbanks AK 99709 US                                            |
| 14441 | FOLA 020817-ROS -                                                                                                                     |
| 14541 | FOLA 030117-ALT -                                                                                                                     |
| 14461 | FOLA 031517-PTE -                                                                                                                     |
| 14581 | FOLA 032117-PLTR -                                                                                                                    |
| 14462 | FOLA 051717-APPT -                                                                                                                    |
| 5443  | Fort Lauderdale Global Entry Enrollment Center - 1800 Eller Drive Suite 104 Ft Lauderdale FL 33316 US                                 |
| 14241 | FTGBL2017 -                                                                                                                           |
| 14081 | GenElect2017 - This is a private event.                                                                                               |
| 9101  | Grand Portage - 9403 E Highway 61 Grand Portage MN 55605 US                                                                           |
| 9140  | Guam International Airport - 355 Chalan PasaHeru Suite B 224-B Tamuning GU 96913 US                                                   |
| 14501 |  GULFAERO -                                                                                                                           |
| 14481 | Gulfport-Biloxi Global Entry Enrollment Center - Gulfport-Biloxi International Airport 14035 Airport Road                             |
| 5031  | Halifax Enrollment Center - U.S. Customs and Border Protection 1 Bell Boulevard  Comp  1666 Halifax Intl Airport                      |
| 5001  | Hidalgo Enrollment Center - 5911 SOUTH STEWART RD   MISSION TX 78572 US                                                               |
| 5340  | Honolulu Enrollment Center - 300 Rodgers Blvd Honolulu HI 96819 US                                                                    |
| 5101  | Houlton Enrollment Center - 1403 Route 95 Belleville NB E7M4Z9 CA                                                                     |
| 7620  | Houston Central Library - 500 McKinney St. Houston TX 77002 US                                                                        |
| 5141  | Houston Intercontinental Global Entry EC - 3870 North Terminal Road Terminal E Houston TX 77032 US                                    |
| 7480  |  Houston Term E - BOARDING PASS REQUIRED TO ENT     - Sterile Corridor requires Boarding Pass IAH Terminal E                          |
| 14242 | HU-GSS1   -                                                                                                                           |
| 14243 | HU-GSS2 -                                                                                                                             |
| 5160  | International Falls Enrollment Center - 312 Highway 11 East International Falls MN 56649 US                                           |
| 14181 | International Falls Global Entry Enrollment Center - 312 Highway 11 East International Falls MN 56649                                 |
| 5140  | JFK International Global Entry EC - JFK International Airport Terminal 4 IAT Jamaica NY 11430 US                                      |
| 12781 | Kansas City Enrollment Center - 90 Beirut Circle Terminal C Gate 90 Kansas City MO 64153 US                                           |
| 5520  | Lansdowne ON  - 664 Highway 137 Hill Island Lansdowne ON K0E1L0 CA                                                                    |
| 5004  | Laredo Enrollment Center - 0 Lincoln Juarez Bridge Bldg.2 Laredo TX 780443130 US                                                      |
| 5360  | Las Vegas Enrollment Center - 5757 Wayne Newton Blvd Terminal 3 Las Vegas NV 89119 US                                                 |
| 14561 | LMT2017 -                                                                                                                             |
| 13561 | London - US Embassy - 24 Grosvenor Square US Embassy London W1A 2LQ GB                                                                |
| 8920  | Los Angeles -Long Beach Seaport  - 301 E. Ocean Blvd  Room 805 Long Beach CA 90802 US                                                 |
| 5180  | Los Angeles International Global Entry EC - 380 World Way Tom Bradley International Terminal Los Angeles                              |
| 13621 | Memphis International Airport Global Enrollment Ce - 2491 Winchester Suite 230 Memphis TN 38116 US                                    |
| 5181  | "Miami International Global Entry EC - 4200 NW 21st Street Miami International Airport Conc. ""J"" Miami"                             |
| 7740  | Milwaukee Enrollment Center - 4915 S Howell Ave. 2nd floor Milwaukee WI 53207 US                                                      |
| 6840  | Minneapolis - St. Paul Global Entry EC - 4300 Glumack Drive St. Paul MN 55111 US                                                      |
| 11000 | Moline Quad Cities International Airport - 3300 69th Ave Quad Cities International Airport Moline IL 61265                            |
| 5028  | Montreal Enrollment Center - 1 Pierre E Trudeau International Airport  975  Blvd Romeo Vachon. Room T1476                             |
| 10260 | Nashville Enrollment Center - 612 Hangar Lane Suite 114 Nashville TN 37217 US                                                         |
| 9740  | New Orleans Enrollment Center - 900 Airline Drive Kenner LA 70062 US                                                                  |
| 5444  |  Newark Global Entry Enrollment Center - Newark Liberty International Airport Terminal B - International Arrivals Area                |
| 5161  | Niagara Falls Enrollment Center - 2250 WHIRLPOOL ST. NIAGARA FALLS NY 14305 US                                                        |
| 14401 | NIKE2017 -                                                                                                                            |
| 5007  | Nogales Enrollment Center - 9 N. GRAND AVENUE NOGALES AZ 85621 US                                                                     |
| 5380  | Orlando Global Entry Enrollment Center - 1 Orlando International Airport Airport Blvd Orlando FL 32827                                |
| 5025  | Ottawa Enrollment Center - 140 Thad Johnson Private Suite 102 Ottawa Cargo Services Ottawa ON K1V0R4                                  |
| 5100  | Pembina Enrollment Center - 10980 Interstate 29 N Pembina ND 58271 US                                                                 |
| 11002 | Peoria International Airport - 5701 W. Smithville Road  Suite 700 Bartonville IL 61607 US                                             |
| 5445  | Philadelphia Global Entry Enrollment Center - PHILADELPHIA INTL AIRPORT TERMINAL A WEST 3RD FLOOR PHILADELPHIA                        |
| 7160  | Phoenix Sky Harbor Global Entry Enrollment Center - CBP-Global Enrollment Center 3400 E. Sky Harbor Blvd                              |
| 9200  | Pittsburgh International Airport - 1000 Airport Boulevard Ticketing Level Pittsburgh PA 15231 US                                      |
| 11841 | Port Clinton Ohio Enrollment Center - 709 S.E. Catawba Road Port Clinton OH 43452 US                                                  |
| 5024  | Port Huron Enrollment Center - 2321 NEXUS Enrollment Center Pine Grove Ave. Port Huron MI 48060 US                                    |
| 7960  | Portland OR Enrollment Center - 7000 PDX AIRPORT Room T3352 Portland OR 97218 US                                                      |
| 14261 | RGBOS2017 -                                                                                                                           |
| 11001 | Rockford-Chicago International Airport - 50 Airport Drive Chicago Rockford International Airport Rockford                             |
| 13981 |  RTAA Board -                                                                                                                         |
| 7600  | Salt Lake City International Airport - 3850 West Terminal Dr International Arrivals Terminal Salt Lake City                           |
| 7520  | San Antonio International Airport - 9800 Airport Boulevard Suite 1101 San Antonio TX 78216 US                                         |
| 5002  | San Diego -Otay Mesa Enrollment Center - 2500 Paseo Internacional San Diego CA 92154 US                                               |
| 13541 | San Diego International Airport - 3707 N Harbor Drive San Diego CA 92101 US                                                           |
| 5446  | San Francisco Global Entry Enrollment Center - San Francisco International Airport San Francisco CA 94128                             |
| 5400  | San Juan Global Entry Enrollment Center - Luis Munoz Marin Int'l Airport Carolina PR 00937 US                                         |
| 5460  | San Luis Enrollment Center - 0 SLU II Global Enrollment Center 1375 South Avenue E San Luis AZ 85349                                  |
| 8060  | San Ysidro Enrollment Center - 405 VIRGINIA AVE SAN YSIDRO CA 92173 US                                                                |
| 5447  | Sanford Global Entry Enrollment Center - 1100 Red Cleveland Blvd Sanford FL 32773 US                                                  |
| 5080  | Sault Ste Marie Enrollment Center - 900 International Bridge Plaza Sault Ste. Marie MI 49783 US                                       |
| 5420  |  SeaTac International Airport Global Entry EC - CBP Global Entry Office  SeaTac International Airport  Seattle                        |
| 5040  | Seattle Urban Enrollment Center - 7277 PERIMETER ROAD SOUTH  RM 116 KING COUNTY INTERNATIONAL AIRPORT BOEING FIELD                    |
| 9040  | Singapore U.S. Embassy - U.S. Embassy 27 Napier Road Singapore SG                                                                     |
| 12021 | St. Louis Enrollment Center - 10701 Lambert Intl Blvd Terminal 2   St. Louis MO 63145 US                                              |
| 5120  | Sweetgrass Enrollment Center - 39825 FAST Enrollment Center 39825 Interstate 15 North Sweetgrass MT 59484                             |
| 8020  | Tampa Enrollment Center - Tampa International Airport 4100 George J Bean Outbound Pkwy Tampa FL 33607                                 |
| 5027  | Toronto Enrollment Center - 6301 Silver Dart Drive  Terminal One-Depatures Level Mississauga ON L5P1B2                                |
| 12421 | Toronto Enrollment Center AESC - 2935 Convair Drive Airport Emergency Support Centre  Mississauga ON L5P1B2                           |
| 14143 | Travel AAA - 10220 Regency Circle Marriott Regency Hotel Omaha NE 68114 US                                                            |
| 14142 | Travel and Transport  - 16950 Wright Plaza Suite 151 Travel Design Lounge by Travel and Transport                                     |
| 9240  | Tucson Enrollment Center - 7150 S. Tucson Blvd Tucson AZ 85756 US                                                                     |
| 6480  | U.S. Custom House - Bowling Green - 1 BOWLING GREEN NEW YORK NY 10004 US                                                              |
| 5026  | Vancouver Enrollment Center - 3211 Grant McConachie Way Vancouver International Airport Richmond BC V7B1Y9                            |
| 5041  | Vancouver Urban Enrollment Center - 1611 Main Street 4th Floor VANCOUVER BC V6A2W5 CA                                                 |
| 5060  | Warroad Enrollment Center  - 41059 Warroad Enrollment Center State Hwy 313 N Warroad MN 56763 US                                      |
| 9300  | Warwick RI Enrollment Center - Warwick RI Enrollment Center 300 Jefferson Boulevard Suite 106 Warwick                                 |
| 5142  | Washington Dulles International Global Entry EC - 22685 International Arrivals- Main Terminal Washington Dulles International Airport |
| 8120  | Washington DC Enrollment Center - 1300 Pennsylvania Avenue NW Washington DC 20229 US                                                  |
| 9260  | West Palm Beach Enrollment Center - West Palm Beach Enrollment Center 1 East 11th Street Third Floor Riviera Beach                    |
| 5029  | Winnipeg Enrollment Center - 1970 Winnipeg NEXUS Office Wellington Room 1074 Winnipeg MB R3H0E3 CA                                    |

# Location codes for other Trusted Traveler programs

Appointments for other programs, including NEXUS, SENTRI, US/Mexico FAST, and US/Canada FAST are available using the same scheduler API as Global Entry. Many sites use the same location id for multiple types of appointments, but some do not (e.g., Blaine, WA is 5020 for Nexus Appointments and 13321 for Global Entry; Ft. Erie is 5228 for US/Canada FAST and 5022) so it is best to consult the lists below to make sure you are requesting the correct type of appointment.

Retrieve the location list for each type of appointment using the URLs below. Find your desired location, and then use the 'id' field as the 'locationId' in your config file.

 * [NEXUS location list](https://ttp.cbp.dhs.gov/schedulerapi/locations/?temporary=false&inviteOnly=false&operational=true&serviceName=NEXUS)

 * [SENTRI location list](https://ttp.cbp.dhs.gov/schedulerapi/locations/?temporary=false&inviteOnly=false&operational=true&serviceName=SENTRI)

 * [US/Mexico FAST location list](https://ttp.cbp.dhs.gov/schedulerapi/locations/?temporary=false&inviteOnly=false&operational=true&serviceName=U.S.%20%2F%20Mexico%20FAST)

 * [US/Canada FAST location list](https://ttp.cbp.dhs.gov/schedulerapi/locations/?temporary=false&inviteOnly=false&operational=true&serviceName=U.S.%20%2F%20Canada%20FAST)

## License
MIT

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
