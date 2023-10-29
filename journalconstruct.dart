import 'dart:io';
import 'dart:math';

import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:recall/Screens/HomePage.dart';

class JournalConstruct extends StatefulWidget {
  @override
  State<JournalConstruct> createState() => _JournalConstructState();
}

class _JournalConstructState extends State<JournalConstruct> {
  @override
  Widget build(BuildContext context) {
    return Card(
      margin: EdgeInsets.all(16.0),
      child: Padding(
        padding: EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(
              'Construct your Timeline',
              style: TextStyle(fontWeight: FontWeight.bold, fontSize: 16.0),
            ),
            SizedBox(height: 8.0),
            Text(
              'Upload from Album',
              style: TextStyle(fontWeight: FontWeight.bold, fontSize: 13.0),
            ),
            SizedBox(height: 8.0),
            Text(
              'Journal your location from your photos and videos',
              style: TextStyle(fontWeight: FontWeight.w300, fontSize: 8.0),
            ),
            SizedBox(height: 8.0),
            Text(
              'Select "Allow Access to all Photos" in the next pop-up to retrieve your photo timestamp and location data in your Recall journal.',
              style: TextStyle(fontSize: 8.0),
            ),
            ElevatedButton(
              onPressed: () {
                Navigator.push(context,
                    MaterialPageRoute(builder: (context) => HomePage()));
              },
              child: Text("Next"),
            ),
          ],
        ),
      ),
    );
  }
}
