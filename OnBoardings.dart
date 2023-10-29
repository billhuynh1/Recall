import 'dart:html';

import 'package:flutter/material.dart';
import 'package:flutter/rendering.dart';

class Onboardings extends StatefulWidget {
  @override
  _OnboardingsState createState() => _OnboardingsState();
}

class _OnboardingsState extends State<_OnboardingsState> {
  final List<String> texts = [
    "Recall is your automatic life journal where you always have an accurate record of your past.",
    "Access the map to see all the places you have visited in a given day, month, year or all times to come.",
    "The timeline shows a day in your life or a bird's eye view of where you spend most of your time.",
    "Talk to your life journal using the Recall Bot. Control when your life journal is recording through your profile."
  ];
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Recall App'),
      ),
      body: PageView.builder(
        itemCount: texts.length,
        itemBuilder: (context, index) {
          return RoundSquareBox(
            text: texts[index],
          );
        },
      ),
    );
  }
}

class RoundSquareBox extends StatelessWidget {
  final String text;

  RoundSquareBox({required this.text});

  @override
  Widget build(BuildContext context) {
    var texts;
    return Container(
      margin: EdgeInsets.all(20.0),
      decoration: BoxDecoration(
        color: Colors.blue,
        borderRadius: BorderRadius.circular(20.0),
      ),
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Text(
            text,
            style: TextStyle(color: Colors.white),
            textAlign: TextAlign.center,
          ),
          SizedBox(height: 20.0),
          Row(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              IconButton(
                icon: Icon(Icons.arrow_left),
                onPressed: () {
                  // Implement logic to move to the previous box
                },
                color: Colors.white,
              ),
              Row(
                children: List.generate(
                  texts.length,
                  (index) => Container(
                    margin: EdgeInsets.symmetric(horizontal: 5.0),
                    width: 10.0,
                    height: 10.0,
                    decoration: BoxDecoration(
                      shape: BoxShape.circle,
                      color: index == 0 ? Colors.white : Colors.grey,
                    ),
                  ),
                ),
              ),
              IconButton(
                icon: Icon(Icons.arrow_right),
                onPressed: () {
                  // Implement logic to move to the next box
                },
                color: Colors.white,
              ),
            ],
          ),
        ],
      ),
    );
  }
}
