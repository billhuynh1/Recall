import 'package:flutter/material.dart';
import 'package:timeline_tile/timeline_tile.dart';

class TimelinePage extends StatefulWidget {
  @override
  State<TimelinePage> createState() => _TimelinePageState();
}

class _TimelinePageState extends State<TimelinePage> {
  @override
  Widget build(BuildContext context) {
     return Scaffold(
       body: Container(
         width: MediaQuery.of(context).size.width,
         child: ListView.builder(
           physics: AlwaysScrollableScrollPhysics(),
           itemCount: 2,
           itemBuilder: (context, index) {
             return Padding(
               padding: const EdgeInsets.only(left: 50),
               child: TimelineTile(
                 beforeLineStyle: LineStyle(
                   color: Colors.black,
                   thickness: 5.5,
                 ),
                 afterLineStyle: LineStyle(
                   color: Colors.black,
                   thickness: 5.5, 
                 ), 
                 indicatorStyle: const IndicatorStyle(
                   width: 35,  
                   color: Colors.black,
                   indicatorXY: 0.1,
                 ),
               ),
             );
           },  
       ),
      ),
    
   }
}