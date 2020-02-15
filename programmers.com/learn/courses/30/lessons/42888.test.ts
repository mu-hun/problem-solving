import { solution } from './42888'

test('sample', () => {
  expect(
    solution([
      'Enter uid1234 Muzi',
      'Enter uid4567 Prodo',
      'Leave uid1234',
      'Enter uid1234 Prodo',
      'Change uid4567 Ryan'
    ])
  ).toEqual([
    'Prodo님이 들어왔습니다.',
    'Ryan님이 들어왔습니다.',
    'Prodo님이 나갔습니다.',
    'Prodo님이 들어왔습니다.'
  ])
})
