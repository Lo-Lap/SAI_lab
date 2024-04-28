from GameField import *
from enum import Enum


class Ant:
    STATES_COUNT = 8
    CHROMOSOME_LENGTH = 83

    BITS_IN_STATE_C = 3
    BITS_IN_ACTION_C = 2

    def __init__(self, chromosome: list):
        if len(chromosome) != Ant.CHROMOSOME_LENGTH:
            raise RuntimeError("Incorrect chromosome length!")

        self.chromosome = chromosome
        self.states = [Ant.State(i) for i in range(Ant.STATES_COUNT)]
        self.curState = None
        self.chromosomePos = 0

        self.chromosomePos = Ant.BITS_IN_STATE_C
        for state in self.states:
            self.readReaction(state, GameField.Cell.EMPTY)
            self.readReaction(state, GameField.Cell.APPLE)

        self.chromosomePos = 0
        self.curState = self.states[self.castToStateNum(self.chromosome, self.chromosomePos)]

    def getAction(self, inAct):
        nextAction = self.curState.getNextAction(inAct)
        self.curState = self.states[self.curState.getNextStateNum(inAct)]
        return nextAction

    def readReaction(self, state, forwardCell):
        state.addNextState(forwardCell, self.castToStateNum(self.chromosome, self.chromosomePos))
        self.chromosomePos += self.BITS_IN_STATE_C
        state.addAction(forwardCell, self.castToAction(self.chromosome, self.chromosomePos))
        self.chromosomePos += self.BITS_IN_ACTION_C

    @staticmethod
    def castToAction(bitCode, pos):
        if not bitCode[pos] and not bitCode[pos + 1]:
            return Ant.Action.MOVE_FORWARD
        elif not bitCode[pos]:
            return Ant.Action.TURN_LEFT
        elif not bitCode[pos + 1]:
            return Ant.Action.TURN_RIGHT
        else:
            return Ant.Action.NO

    @staticmethod
    def castToStateNum(bitCode: list, pos: int):
        res = 0
        if bitCode[pos]:
            res += 4

        if bitCode[pos + 1]:
            res += 2

        if bitCode[pos + 2]:
            res += 1

        return res

    class Action:
        MOVE_FORWARD, TURN_LEFT, TURN_RIGHT, NO = range(4)

    class State:
        num = 0
        nextStateNum = dict()
        nextAction = dict()

        def __init__(self, num):
            self.num = num

        def addNextState(self, forwCell, nextStateNum: int):
            self.nextStateNum[forwCell] = nextStateNum

        def addAction(self, forwCell, action):
            """action из class Action"""
            self.nextAction[forwCell] = action

        def getNextStateNum(self, forwardCell) -> int:
            return self.nextStateNum[forwardCell]

        def getNextAction(self, forwardCell):
            return self.nextAction[forwardCell]

        def getNum(self):
            return self.num
