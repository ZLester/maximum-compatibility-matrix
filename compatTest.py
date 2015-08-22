import unittest
import compat

class participantTestCase(unittest.TestCase):
  def setUp(self):
    self.participant = compat.Participant('Eric')
    self.friend = compat.Participant('John')
    self.enemy = compat.Participant('Spike')

  def test_participant_name(self):
    self.assertEqual(self.participant.name, 'Eric')

  def test_participant_likes(self):
    self.assertIsInstance(self.participant.likes, list)

  def test_participant_dislikes(self):
    self.assertIsInstance(self.participant.dislikes, list)

  def test_participant_add_likes(self):
    self.participant.like(self.friend)
    self.assertEqual(len(self.participant.likes), 1)
    self.assertIsInstance(self.participant.likes[0], compat.Participant)

  def test_participant_add_dislikes(self):
    self.participant.dislike(self.enemy)
    self.assertEqual(len(self.participant.dislikes), 1)
    self.assertIsInstance(self.participant.dislikes[0], compat.Participant)

class cohortTestCase(unittest.TestCase):
  def setUp(self):
    self.cohort = compat.Cohort()

  def test_cohort_exists(self):
    self.assertIsInstance(self.cohort, compat.Cohort)

  def test_cohort_has_list_of_participants(self):
    self.assertIsInstance(self.cohort.participants, list)

  def test_cohort_can_add_participant(self):
    participant = compat.Participant('Eric')
    self.cohort.addParticipant(participant)
    self.assertEqual(self.cohort.participants[0].name, 'Eric')